import requests
import random
import time

url = "https://asifiqbalasds.app.n8n.cloud/webhook/traffic-signal"

traffic_levels = ["LOW", "MEDIUM", "HIGH"]
nearby_levels = ["LOW", "MEDIUM", "HIGH"]

while True:
    data = {
        "traffic_level": random.choice(traffic_levels),
        "emergency": random.choice([False, False, False, True]),
        "nearby": random.choice(nearby_levels),
        "signal_id": "DHK-" + str(random.randint(1, 5))
    }

    try:
        res = requests.post(url, json=data)
        print("Sent:", data)
        print("Response:", res.json())
    except Exception as e:
        print("Error:", e)

    time.sleep(3)