import psutil
import json
from google.cloud import pubsub_v1

PROJECT_ID = "southern-ivy-498911-g8"
TOPIC_ID = "cloud-monitor-alerts"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

cpu = psutil.cpu_percent()
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

data = {
    "cpu": cpu,
    "ram": ram,
    "disk": disk
}

with open("data.json", "w") as f:
    json.dump(data, f)

if cpu > 1 or ram > 80 or disk > 80:

    alert = f"""
ALERT GENERATED

CPU: {cpu}%
RAM: {ram}%
DISK: {disk}%
"""

    publisher.publish(
        topic_path,
        alert.encode("utf-8")
    )

    print("Alert Published")
