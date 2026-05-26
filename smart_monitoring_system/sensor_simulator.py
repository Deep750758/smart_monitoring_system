import random
import time
import json
from kafka import KafkaProducer

# Create Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Send data continuously
while True:
    temp = random.randint(20, 100)

    data = {
        "temperature": temp
    }

    print("Sending:", data)

    producer.send("sensor-data", data)

    time.sleep(2)