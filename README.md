# Hotel Booking Data Processing & Retrieval System

## Project Overview

This project is designed to **process hotel booking data** and enable **efficient retrieval** using a **Retrieval-Augmented Generation (RAG)** approach. It utilizes **FAISS (Facebook AI Similarity Search)** for similarity search and **Sentence Transformers** to generate text embeddings. The system allows users to query hotel booking information using natural language and retrieve relevant booking details.

The backend is built with **FastAPI**, providing a scalable and efficient REST API. The entire development has been done on **Google Colab**, allowing for cloud-based execution and deployment.

---

## Purpose

The primary goals of this project are:

- **Efficiently process and store hotel booking data**
- **Enable natural language search for booking information**
- **Deploy a REST API for seamless data retrieval**
- **Provide analytics on revenue, cancellations, and booking trends**

This system can be used by:

- **Hotel management teams** for better decision-making
- **Travel agencies** analyzing customer booking behavior
- **Researchers** studying hospitality trends

---

## System Workflow

### 1. **Data Processing**
- Loads and processes hotel booking data from a CSV file
- Extracts key attributes and creates structured text representations
- Generates vector embeddings using **Sentence Transformers**
- Stores embeddings in a **FAISS index** for fast retrieval

### 2. **Query Processing and Retrieval**
- Converts a user's **natural language query** into an embedding
- Searches the **FAISS index** for the most relevant results
- Returns structured booking details with **similarity scores**

### 3. **API Deployment Using FastAPI**
- The backend is powered by **FastAPI**, exposing REST endpoints
- Users can search for bookings and retrieve relevant results
- An analytics endpoint provides insights on revenue, cancellations, and lead times

---

## Running the Project

### Running on Google Colab
1. Open **Google Colab** and upload the required files (**dataset, FAISS index, metadata**).
2. Install dependencies:

   ```bash
   !pip install pandas numpy faiss-cpu sentence-transformers fastapi uvicorn pyngrok
3. Execute the provided Colab script to:
   Process and embed the dataset
   Save metadata and create the FAISS index
   Deploy the FastAPI server
   Use ngrok to expose the API and generate a public URL
   Send queries to the /ask endpoint to retrieve relevant booking information

## Running on a Local Machine
 1.Clone the repository:
   ```bash
   git clone https://github.com/your-username/hotel-booking-retrieval.git
   cd hotel-booking-retrieval
 2.Install dependencies:
   ```bash
   pip install -r requirements.txt

 3.Start the FastAPI server:
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000 --reload

 4.Access the API documentation at:
   ```bash
   http://127.0.0.1:8000/docs

Use the available endpoints to query the booking database

**Conclusion**
This project demonstrates how NLP and vector-based retrieval can improve hotel booking analysis. Users can query the system using natural language and receive relevant results efficiently. This system is useful for hotel managers, travel agencies, and researchers studying booking trends.
Contributions and suggestions are welcome. 
