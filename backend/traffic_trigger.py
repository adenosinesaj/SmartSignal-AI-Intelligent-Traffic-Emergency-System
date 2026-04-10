import requests
import random
import time
from datetime import datetime

url = "https://asifiqbalasds.app.n8n.cloud/webhook/traffic-signal"

traffic_levels = ["LOW", "MEDIUM", "HIGH"]
nearby_levels = ["LOW", "MEDIUM", "HIGH"]

def get_priority_score(traffic, emergency, nearby):
    score = 0

    # Traffic weight
    if traffic == "HIGH":
        score += 3
    elif traffic == "MEDIUM":
        score += 2
    else:
        score += 1

    # Emergency override
    if emergency:
        score += 10

    # Nearby influence
    if nearby == "HIGH":
        score += 2
    elif nearby == "LOW":
        score += 1

    return score


while True:
    signals = []

    # 🔥 Generate 4 signals at once
    for i in range(1, 5):
        signal = {
            "signal_id": f"DHK-{i}",
            "traffic_level": random.choice(traffic_levels),
            "emergency": random.choice([False, False, False, True, False, False, False]),
            "nearby": random.choice(nearby_levels)
        }

        # Calculate priority
        signal["priority"] = get_priority_score(
            signal["traffic_level"],
            signal["emergency"],
            signal["nearby"]
        )

        signals.append(signal)

    # 🎯 Pick highest priority signal
    best_signal = max(signals, key=lambda x: x["priority"])

    # ⏱️ Add current date & time
    now = datetime.now()
    best_signal["date"] = now.strftime("%Y-%m-%d")
    best_signal["time"] = now.strftime("%H:%M:%S")

    # 🔗 Send to n8n
    try:
        res = requests.post(url, json=best_signal)

        print("\n===== ALL SIGNALS =====")
        for s in signals:
            print(s)

        print("\n🚦 SELECTED SIGNAL:")
        print(best_signal)

        print("\n📩 RESPONSE:")
        print(res.json())

    except Exception as e:
        print("Error:", e)

    time.sleep(5)