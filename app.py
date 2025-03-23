from fastapi import FastAPI
import faiss
import numpy as np
import json
from sentence_transformers import SentenceTransformer
import pandas as pd
from fastapi.responses import JSONResponse

app = FastAPI()

# Load Model and FAISS Index
model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("faiss_booking_index.idx")

with open("booking_metadata.json", "r") as f:
    metadata = json.load(f)

def format_result(raw_text, score):
    fields = [
        "hotel_type", "unknown_1", "customer_id", "year", "month", "day",
        "nights", "unknown_2", "unknown_3", "meal_plan", "hotel_category",
        "booking_channel", "booking_type", "customer_segment",
        "price", "unknown_4", "status"
    ]
    values = raw_text.split(" | ")
    formatted = dict(zip(fields, values))
    formatted["score"] = round(score, 4)
    formatted["customer_id"] = int(formatted["customer_id"])
    formatted["date"] = f"{formatted['year']}-{formatted['month'].zfill(2)}-{formatted['day'].zfill(2)}"
    formatted["nights"] = int(formatted["nights"])
    formatted["price"] = float(formatted["price"])
    formatted.pop("unknown_1", None)
    formatted.pop("unknown_2", None)
    formatted.pop("unknown_3", None)
    formatted.pop("unknown_4", None)
    formatted.pop("year", None)
    formatted.pop("month", None)
    formatted.pop("day", None)
    formatted.pop("booking_type", None)
    return formatted

from fastapi.responses import JSONResponse

@app.post("/ask")
def ask_question(query: str, top_k: int = 5):
    query_embedding = model.encode([query], convert_to_numpy=True)
    distances, indices = index.search(query_embedding, top_k)

    results = [
        format_result(metadata[str(idx)], float(distances[0][i]))
        for i, idx in enumerate(indices[0])
    ]
    
    return JSONResponse(content={"results": results}, media_type="application/json", headers={"Content-Type": "application/json"})


@app.post("/analytics")
def get_analytics():
    df = pd.read_csv("/mnt/data/cleaned_hotel_bookings.csv")
    analytics = {
        "total_revenue": df["adr"].sum(),
        "cancellation_rate": (df["is_canceled"].sum() / len(df)) * 100,
        "avg_lead_time": df["lead_time"].mean(),
    }
    return analytics

@app.get("/health")
def health_check():
    return {"status": "running"}
