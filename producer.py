import time
import uuid
import json
from redis_client import redis_client
QUEUE_NAME="task_queue"
for i in range(6):
    task_id=str(uuid.uuid4())
    task_data={
        "id":task_id,
        "data":f"Task-{i}",
        "status":"pending"
    }
    redis_client.set(f"task:{task_id}",json.dumps(task_data))
    redis_client.rpush(QUEUE_NAME,task_id)
    print(f"[Producer] Added {task_id}")
    time.sleep(1)
print("All tasks added.")
