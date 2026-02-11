# Disaster-Management-MLOps

An end-to-end Docker-based MLOps microservices system for disaster message classification.
This project demonstrates manual Docker networking, service-to-service communication,
and ML model serving using a clean, production-style architecture.

---

## Project Overview

During disaster events (floods, earthquakes, cyclones, etc.), large volumes of textual messages are generated. This system classifies disaster-related messages using a trained ML model and exposes predictions through a microservices-based MLOps pipeline.
Each component (UI, API, ML inference, Database) runs in an isolated Docker container connected via a manually created Docker network.

---

## Architecture Overview

Streamlit UI → API Service → ML Service
                              ↓
                           Database

Key principles:
- Docker DNS–based service discovery
- No hard-coded IP addresses
- No localhost usage inside containers
- Explicit user-defined Docker network

---

## Docker Networking (Core Requirement)

This project explicitly implements manual Docker networking.

Network details:
- Network name: mlops-net
- Driver: bridge
- Network created manually using Docker CLI
- Docker Compose uses this network as an external network

This ensures the system does not rely on Docker’s default networking.

---

## Project Folder Structure
```bash
Disaster-Management-MLOps/
├── api/
│   ├── app.py
│   ├── config.py
│   ├── db.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── ml/
│   ├── predict.py
│   ├── model_loader.py
│   ├── models/
│   ├── training/
│   ├── Dockerfile
│   └── requirements.txt
│
├── database/
│   ├── init.sql
│   └── Dockerfile
│
├── streamlit/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docker-compose.yml
├── README.md
└── .gitignore
```
---

## Technology Stack

Infrastructure & DevOps:
- Docker
- Docker Compose
- User-defined Docker bridge network

Backend & ML:
- Python 3.11
- Flask / FastAPI
- scikit-learn
- joblib
- pandas
- numpy
- requests

Database:
- PostgreSQL

Frontend:
- Streamlit

---

## How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/Het1014/Disaster-Management-MLOps
cd Disaster-Management-MLOps
```

### 2. Create Docker network manually
```bash
docker network create mlops-net
```
### 3. Build services
```bash
docker compose build
```
### 4. Start all services
```bash
docker compose up -d
```
### 5. Verify network attachment
```bash
docker network inspect mlops-net
```
---

## Verifying Inter-Service Communication

Enter the API container:
```bash
docker compose exec api-service sh
```
Test ML service using Python:
```bash
python
import requests
requests.get("http://ml-service:5000")
```
Expected output:
<Response [404]>

A 404 response confirms successful Docker DNS resolution and inter-container connectivity.

---

## Service Endpoints

Streamlit UI: http://localhost:8501
API Service: http://localhost:8000
ML Service: Internal only (ml-service:5000)
Database: Internal only (db:5432)

---

## Stopping and Starting Containers

Stop all containers (without removing):
```bash
docker compose stop
```
Start containers again:
```bash
docker compose start
```
Stop a single container:
```bash
docker stop <container_name>
```
---

## Viewing Logs
```
docker compose logs api-service
docker compose logs ml-service
docker compose logs db
docker compose logs streamlit
```
---

## Important Notes

- Containers communicate using service names, not IP addresses
- Minimal Docker images are used
- ML and Database services are not publicly exposed
- Host ports are used only for UI and API access

---

## Key Takeaways

- Manual Docker network implementation
- External network usage in Docker Compose
- Microservices-based ML architecture
- Production-style isolation and communication
- Application-level verification of networking

---

## Conclusion

This project demonstrates a real-world MLOps microservices system with explicitly managed
Docker networking, clear separation of concerns, and scalable deployment design.
