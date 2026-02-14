# ⚡ Mini Distributed Task Queue

A lightweight distributed background job processing system built using FastAPI, Redis, and Python workers.  
This project demonstrates real-world backend architecture including async processing, task queues, and scalable worker systems.

---

## 🚀 Overview

Modern applications offload heavy tasks to background workers.  
This project implements a minimal version of that architecture using:

- FastAPI as the API layer
- Redis as the message broker
- Python workers for async processing

---

## 🏗 Architecture

Client → FastAPI → Redis Queue → Worker(s) → Redis Task State

### Flow
1. Client submits a task via REST API
2. API stores metadata in Redis
3. Task ID pushed into Redis queue
4. Worker pulls task asynchronously
5. Worker updates task status

---

## ✨ Features

- Async background job execution
- Redis-backed distributed queue
- Multi-worker parallel processing
- Task lifecycle tracking
- Modular architecture
- Easy to extend

---

## 🛠 Tech Stack

- Backend: FastAPI  
- Queue: Redis  
- Language: Python  
- Server: Uvicorn  

---

## 📂 Project Structure

api.py              - FastAPI application  
worker.py           - Background worker  
redis_client.py     - Redis connection layer  
inspector.py        - Task inspection tool (optional)  
requirements.txt    - Dependencies  

---

## ⚙️ Setup & Run Locally

### 1. Clone Repo
git clone https://github.com/YOUR_USERNAME/mini-distributed-queue.git  
cd mini-distributed-queue

---

### 2. Install Dependencies
pip install -r requirements.txt

---

### 3. Start Redis (Docker recommended)
docker run -p 6379:6379 redis
alternate use wsl->sudo service redis-server start

---

### 4. Start Worker
python worker.py

---

### 5. Start API
uvicorn api:app --reload

---

### 6. Open API Docs
http://127.0.0.1:8000/docs

---

## 📡 API Endpoints

Create Task  
POST /task  
Returns: task_id and submission status

Get Task Status  
GET /task/{task_id}  
Returns current task state

---

## 🧠 Concepts Demonstrated

- Producer–Consumer pattern  
- Distributed workers  
- Message queues  
- Async processing  
- Task state management  
- Horizontal scaling basics  

---

## 🚀 Future Improvements

- Task result storage  
- Retry mechanisms  
- Priority queues  
- Docker Compose setup  
- Cloud deployment  
- Web dashboard  
- AI task processing  

---

## 👨‍💻 Author

Built as a hands-on exploration of distributed backend systems and async architecture.

If you found this useful, consider starring the repo ⭐

---

## 📜 License
MIT License
