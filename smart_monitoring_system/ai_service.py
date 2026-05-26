from kafka import KafkaConsumer
import json

# Create Kafka Consumer
consumer = KafkaConsumer(
    'sensor-data',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("AI Service Started...")

# Read messages continuously
for message in consumer:
    data = message.value

    temperature = data["temperature"]

    print("Received:", data)

    # AI Logic
    if temperature > 70:
        print("ALERT: High Temperature Detected")
    else:
        print("Temperature Normal")