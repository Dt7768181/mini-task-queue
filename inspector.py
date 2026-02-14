import json 
from redis_client import redis_client
keys=redis_client.keys("task:*")
print(f"Found {len(keys)} tasks\n")
for key in keys:
    task=json.loads(redis_client.get(key))
    print(task)