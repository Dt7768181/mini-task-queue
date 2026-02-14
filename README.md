# Mini Distributed Task Queue 🚀

A lightweight distributed background job processing system built using FastAPI, Redis, and Python workers.

## Features
- Async task submission via REST API
- Redis-based message queue
- Multi-worker processing
- Task status tracking
- Scalable architecture

## Tech Stack
- FastAPI
- Redis
- Python

## How It Works
Client → FastAPI → Redis Queue → Worker → Redis Status

## Run Locally

### 1. Start Redis
```cmd -> type wsl 
sudo service redis-server start

### 2. Start Worker
python worker.py

### 3. Start API
uvicorn api:app --reload

