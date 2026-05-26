# Smart Monitoring System

A real-time smart monitoring system built using:

- Python
- Apache Kafka
- Docker
- FastAPI

This project simulates sensor temperature data, streams it through Kafka, and analyzes it using an AI monitoring service.

---

# Project Architecture

```text
Sensor Simulator → Kafka Producer → Kafka Topic → AI Analyzer Service
```

---

# Features

- Real-time temperature monitoring
- Kafka-based streaming
- AI alert system
- Dockerized environment
- FastAPI backend support
- Simple and scalable architecture

---

# Project Structure

```text
smart_monitoring_system/
│
├── ai_service.py
├── app.py
├── consumer.py
├── producer.py
├── sensor_simulator.py
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

---

# Technologies Used

- Python
- Apache Kafka
- ZooKeeper
- Docker
- FastAPI
- kafka-python

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/your-username/smart_monitoring_system.git

cd smart_monitoring_system
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Start Kafka and ZooKeeper

```bash
docker compose up --build
```

---

## 4. Run Producer

Open a new terminal:

```bash
python producer.py
```

---

## 5. Run AI Service

Open another terminal:

```bash
python ai_service.py
```

---

# Example Output

## Producer

```text
Produced: {'temperature': 85}
```

## AI Service

```text
Received: {'temperature': 85}

ALERT: High Temperature Detected
```

---

# FastAPI

Run FastAPI server:

```bash
uvicorn app:app --reload
```

Open:

```text
http://localhost:8000
```

Swagger Docs:

```text
http://localhost:8000/docs
```

---

# Docker Commands

## Start Containers

```bash
docker compose up --build
```

## Stop Containers

```bash
docker compose down
```

## Check Running Containers

```bash
docker ps
```

---

# Future Improvements

- MongoDB integration
- Machine learning prediction
- Dashboard visualization
- Email/SMS alerts
- Kubernetes deployment
- Cloud deployment

---

# Author

Deep Upwanshi

Email: deepupwanshi46@gmail.com
