import json
import os
import random
import time
from datetime import datetime

from kafka import KafkaProducer

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")
TOPIC = os.getenv("KAFKA_TOPIC", "events")

SENSORS = ["temp", "humidity", "pressure", "vibration"]


def main():
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER,
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )

    while True:
        event = {
            "ts": datetime.utcnow().isoformat(),
            "sensor": random.choice(SENSORS),
            "value": round(random.uniform(0, 100), 2),
            "device": f"device-{random.randint(1, 20)}",
        }
        producer.send(TOPIC, event)
        producer.flush()
        time.sleep(0.2)


if __name__ == "__main__":
    main()

