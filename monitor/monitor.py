import psutil
import json

data = {
    "cpu": psutil.cpu_percent(),
    "ram": psutil.virtual_memory().percent,
    "disk": psutil.disk_usage('/').percent
}

with open("data.json","w") as f:
    json.dump(data,f)

