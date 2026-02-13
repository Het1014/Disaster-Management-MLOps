
# Disaster-Management-MLOps

An end-to-end Docker-based MLOps microservices system for disaster message classification.
This project demonstrates manual Docker networking, service-to-service communication,
ML model serving, and database verification using a production-style architecture.

---

## Project Overview

During disaster events (floods, earthquakes, cyclones, etc.), large volumes of textual messages are generated. 
This system classifies disaster-related messages using a trained ML model and exposes predictions 
through a microservices-based MLOps pipeline.

Each component (UI, API, ML inference, Database) runs in an isolated Docker container connected 
via manually managed Docker networks.

---

## Architecture Overview

Streamlit UI → API Service → ML Service  
                              ↓  
                          Database  

Key principles:

- Docker DNS–based service discovery
- No hard-coded IP addresses
- No localhost usage inside containers
- Explicit user-defined Docker networking
- Optional network segmentation (frontend + backend isolation)

---

## Docker Networking (Core Requirement)

This project explicitly implements manual Docker networking.
Network created manually using Docker CLI
Docker Compose uses this network as an external network

### Primary Network (Single Network Approach)

Network name: `mlops-net`  
Driver: `bridge`  
Created manually using Docker CLI

```bash
docker network create --driver bridge mlops-net
docker network ls
docker network inspect mlops-net
```

All containers were connected to this single network for simplified communication.

---

## Network Segmentation (Advanced Practical)

The system was also tested with two-network segmentation to simulate production isolation.

### Frontend Network
- streamlit
- api-service

### Backend Network
- api-service
- ml-service
- db

This ensured:
- Streamlit cannot directly access Database
- ML service is not exposed to frontend
- API acts as the gateway layer

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

Infrastructure:
- Docker
- Docker Compose
- User-defined Docker bridge networks

Backend & ML:
- Python 3.11
- Flask
- scikit-learn==1.8.0
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

### 1. Clone Repository

```bash
git clone https://github.com/Het1014/Disaster-Management-MLOps
```
```bash
cd Disaster-Management-MLOps
```

### 2. Create Network

```bash
docker network create mlops-net
```

### 3. Build Services

```bash
docker compose build
```

### 4. Start Services

```bash
docker compose up -d
```

If using project namespace:

```bash
docker compose -p disaster_v2 up -d
```

Rebuild and start:

```bash
docker compose -p disaster_v2 up --build -d
```

---

## Verify Network Attachment

```bash
docker network inspect mlops-net
```

---

## Verifying Inter-Service Communication

Enter API container:

```bash
docker compose exec api-service sh
```

Test ML connectivity:

```bash
curl http://ml-service:5000/health
```

Expected successful response confirms DNS resolution.

---

## Database Verification via Terminal (PostgreSQL CLI)

Enter DB container:

```bash
docker compose exec db psql -U admin -d postgres
```

If using project namespace:

```bash
docker compose -p disaster_v2 exec db psql -U admin -d postgres
```

Inside PostgreSQL:

List databases:
```sql
\l
```

Connect to database:
```sql
\c postgres
```

List tables:
```sql
\dt
```

View records:
```sql
SELECT * FROM <table_name>;
```

Limit output:
```sql
SELECT * FROM <table_name> LIMIT 10;
```

Exit PostgreSQL:
```sql
\q
```

---

## Important Docker Commands Used

### Network Commands

```bash
docker network create --driver bridge mlops-net
docker network ls
docker network inspect mlops-net
```

### Container Commands

```bash
docker ps
docker compose ps
docker compose stop
docker compose start
docker compose down
docker compose down -v
docker rm -f <container_name>
```

### Build Commands

```bash
docker build -t ml-container ./ml
docker build --no-cache -t ml-container ./ml
docker compose build
```

### Logs & Debugging

```bash
docker logs <container_name>
docker compose logs api-service
docker compose logs ml-service
docker compose logs db
docker compose logs streamlit
docker compose exec api-service sh
docker compose exec ml-service sh
```

---

## Service Endpoints

Streamlit UI: http://localhost:8501  
API Service: http://localhost:8000  
ML Service: Internal only (ml-service:5000)  
Database: Internal only (db:5432)

---

## Key Takeaways

- Manual Docker network implementation
- Two-network segmentation (frontend + backend)
- Service-name-based communication
- Microservices-based ML deployment architecture

---

## Conclusion

<<<<<<< HEAD
This project demonstrates a MLOps microservices architecture with explicit Docker networking, secure service isolation, database verification via CLI, and scalable container orchestration using Docker Compose.
=======
This project demonstrates a real-world MLOps microservices system with explicitly managed
Docker networking, clear separation of concerns, and scalable deployment design.
>>>>>>> c5752d0ffdcfe08a86d6bd3c430c1cce43ad26ac
