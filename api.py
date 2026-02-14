from fastapi import FastAPI
import uuid
import json
from redis_client import redis_client
app=FastAPI()
QUEUE_NAME="task_queue"
@app.get("/")
def home():
    return {"message":"Mini Task Queue API running"}
@app.post("/task")
def create_task():
    task_id=str(uuid.uuid4())
    task_data={
        "id":task_id,
        "data":"Sample background task",
        "status":"pending"
    }
    redis_client.set(f"task:{task_id}",json.dumps(task_data))
    redis_client.rpush(QUEUE_NAME,task_id)
    return{
        "task_id":task_id,
        "status":"submitted"
    }
@app.get("/task/{task_id}")
def get_task(task_id:str):
    task_json=redis_client.get(f"task:{task_id}")
    if not task_json:
        return {"error":"Task not found"}
    return json.loads(task_json)
