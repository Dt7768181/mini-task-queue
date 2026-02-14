import json
import time
import random
from redis_client import redis_client
QUEUE_NAME="task_queue"
print("Worker started...")
while True:
    _,task_id=redis_client.blpop(QUEUE_NAME)
    task_key=f"task:{task_id}"
    task=json.loads(redis_client.get(task_key))
    task["status"]="running"
    redis_client.set(task_key,json.dumps(task))
    print(f"[Worker] Running {task_id}")
    try:
        if random.random()<0.2:
            raise Exception("Rando failure")
        time.sleep(random.randint(1,3))
        task["status"]="completed"
        redis_client.set(task_key,json.dumps(task))
        print(f"[Worker] copleted {task_id}")
    except Exception as e:
        task["status"]="failed"
        redis_client.set(task_key,json.dumps(task))
        print(f"[Worker] Failed {task_id}:{e}")