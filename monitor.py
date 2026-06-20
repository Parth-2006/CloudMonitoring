import os
import psutil
import json
from google.cloud import pubsub_v1

# Service Account Key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/nirajpawar981/cloud-monitor-key.json"

# GCP Configuration
PROJECT_ID = "southern-ivy-498911-g8"
TOPIC_ID = "cloud-monitor-alerts"

# Pub/Sub Publisher
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

# Collect System Metrics
cpu = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

# Save Metrics for Dashboard
data = {
    "cpu": cpu,
    "ram": ram,
    "disk": disk
}

with open("data.json", "w") as f:
    json.dump(data, f)

print(f"CPU Usage : {cpu}%")
print(f"RAM Usage : {ram}%")
print(f"Disk Usage: {disk}%")

# Alert Threshold
CPU_THRESHOLD = 80
RAM_THRESHOLD = 80
DISK_THRESHOLD = 80

if cpu > CPU_THRESHOLD or ram > RAM_THRESHOLD or disk > DISK_THRESHOLD:

    alert = f"""
ALERT GENERATED

CPU Usage : {cpu}%
RAM Usage : {ram}%
Disk Usage: {disk}%

Threshold Exceeded!
"""

    future = publisher.publish(
        topic_path,
        alert.encode("utf-8")
    )

    print("Alert Published")
    print("Message ID:", future.result())

else:
    print("System Healthy - No Alert Sent")
