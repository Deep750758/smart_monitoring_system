from kafka import KafkaConsumer
import json

# Create Kafka Consumer
consumer = KafkaConsumer(
    'sensor-data',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Read messages continuously
for message in consumer:
    data = message.value

    print("Received:", data)

    temp = data["temperature"]

    if temp > 70:
        print("High Temperature Alert")
    else:
        print("Normal Temperature")