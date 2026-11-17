
# 🚀 Cloud-Native Containerized Microservice (`v2.0.0`) — Docker & Kubernetes Deployment

![Python](https://img.shields.io/badge/Python-3.10--slim-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0.0-black?logo=flask)
![Docker](https://img.shields.io/badge/Docker-Multi--Stage%20Build-2496ED?logo=docker)
![Kubernetes](https://img.shields.io/badge/Kubernetes-v1.36.1-326CE5?logo=kubernetes)
![Security](https://img.shields.io/badge/User-Non--Root%20(appuser)-green)

> **Course:** Cloud Native DevOps — Activity 1  
> **Student:** Yash Dhananjay Dalavi | **PRN:** `202301100017` | **Roll No:** `CCF54`  
> **Branch:** B.Tech Computer Engineering (Software Engineering), MIT Academy of Engineering, Pune  
> **Video Demonstration:** [Watch Walkthrough on Google Drive](https://drive.google.com/file/d/1jPFCUMMWUXK2nCPD80hMkfYeCXdGhVZa/view?usp=sharing)

---

## 📌 Project Overview

This repository demonstrates the end-to-end containerization and Kubernetes orchestration of a **stateless Python Flask microservice (`v2.0.0`)** built on twelve-factor cloud-native principles.

### Key Features

- **Multi-Stage Docker Build:** Separates dependency compilation (`builder` stage) from the minimal runtime stage (`python:3.10-slim`), reducing image size from `200 MB` (`v1.0`) to `190 MB` (`46.4 MB` compressed content size).
- **Container Hardening:** Executes as an unprivileged non-root user (`appuser`) with `.dockerignore` build context filtering and a native Docker `HEALTHCHECK`.
- **Kubernetes High Availability & Self-Healing:** Deployed as a 2-replica `Deployment` with zero-downtime `RollingUpdate` (`maxSurge: 1`, `maxUnavailable: 0`), CPU/memory resource governance, automated HTTP `livenessProbe` and `readinessProbe`, and `NodePort` (`30005`) service discovery.

---

## 🏗️ Architecture & Workflow

```text
[ Developer / GitHub ]
         |
         v
[ Multi-Stage Dockerfile ]
         |
         +----> Stage 1 (builder): pip install --prefix=/install
         |
         +----> Stage 2 (runtime): non-root appuser + HEALTHCHECK
         |
         v
[ cloud-native-app:v2.0 ]
         |
         +----> Imported into containerd (desktop-control-plane)
         |
         v
[ Kubernetes Cluster ]
   |
   +-- Deployment (cloud-app-deployment, replicas: 2, RollingUpdate)
   |      |
   |      +-- Pod 1 (APP_ENV=production, Liveness/Readiness Probes on /health)
   |      |
   |      +-- Pod 2 (APP_ENV=production, Liveness/Readiness Probes on /health)
   |
   +-- Service (cloud-app-service, NodePort 5000:30005/TCP)
```

---

## 📂 Repository Structure

| File | Description |
|---|---|
| `app.py` | Stateless Flask REST microservice exposing `GET /` (with pod hostname `served_by` and `APP_ENV`) and `GET /health`. |
| `requirements.txt` | Pinned Python runtime dependencies (`flask==3.0.0`). |
| `Dockerfile` | Production two-stage Docker build with `appuser` non-root execution, unbuffered logging, and `HEALTHCHECK`. |
| `.dockerignore` | Excludes `__pycache__`, `.git`, YAML manifests, and local docs from the Docker build context. |
| `deployment.yaml` | Declarative Kubernetes Deployment (2 replicas, RollingUpdate, CPU/memory quotas, HTTP health probes). |
| `service.yaml` | Declarative Kubernetes NodePort Service exposing container port 5000 on external port 30005. |
| `README.md` | Complete project architecture, deployment instructions, and verification guide. |

---

## 🔌 API Endpoints

| Method | Endpoint | Response (JSON) | Purpose |
|---|---|---|---|
| GET | `/` | `{"environment":"production","message":"Welcome to Cloud-Native Containerized Application!","served_by":"<pod-hostname>","status":"Success","version":"2.0.0"}` | Returns app metadata and live serving pod hostname for load-balancing verification. |
| GET | `/health` | `{"status":"Healthy"}` (HTTP 200) | Unified health endpoint used by Docker HEALTHCHECK and Kubernetes probes. |

---

## 🐳 Step 1: Local Docker Build & Verification

### 1. Build the Multi-Stage Image

```bash
docker build -t cloud-native-app:v2.0 .
docker images cloud-native-app
```

### 2. Run & Verify Standalone Container

```bash
# Run detached container on port 5000
docker run -d -p 5000:5000 --name cloud-app-container cloud-native-app:v2.0

# Confirm healthy status
docker ps

# Test REST endpoints and verify non-root user (appuser)
curl http://localhost:5000/
curl http://localhost:5000/health
docker exec cloud-app-container whoami

# Clean up standalone container before Kubernetes port-forwarding
docker rm -f cloud-app-container
```

---

## ☸️ Step 2: Kubernetes Deployment & Verification

### 1. Import Local Image into Docker Desktop (kind) Cluster

```bash
docker save cloud-native-app:v2.0 | docker exec -i desktop-control-plane ctr --namespace=k8s.io images import -
```

### 2. Apply Deployment & Service Manifests

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# Verify rollout and active resources
kubectl rollout status deployment/cloud-app-deployment
kubectl get deployment,pods,svc -l app=cloud-app
```

### 3. Inspect Probes, Resource Quotas & Service Endpoints

```bash
kubectl describe pod -l app=cloud-app
kubectl get endpoints cloud-app-service
```

### 4. Access Application via Port Forwarding

```bash
kubectl port-forward svc/cloud-app-service 5000:5000
```

Open the following URLs in your browser:

- http://localhost:5000
- http://localhost:5000/health

---

## 🧪 Step 3: Cloud-Native Capabilities Verification

### 1. Service Load Balancing Across Pods

```bash
kubectl run curl-test --rm -it --image=curlimages/curl --restart=Never -- sh -c "for i in 1 2 3 4 5 6; do curl -s http://cloud-app-service:5000/; echo; done"
```

### 2. Self-Healing Pod Recovery

```bash
kubectl delete pod <pod-name>
kubectl get pods -l app=cloud-app
```

### 3. Elastic Horizontal Scaling (2 → 3 → 2)

```bash
kubectl scale deployment cloud-app-deployment --replicas=3
kubectl get pods -l app=cloud-app

kubectl scale deployment cloud-app-deployment --replicas=2
```

### 4. Real-Time Unbuffered Logging (`PYTHONUNBUFFERED=1`)

```bash
kubectl logs -l app=cloud-app --tail=15
```

---

## 🛠️ Key Troubleshooting Insights

### 1. ErrImagePull on Local Images

Docker Desktop's `desktop-control-plane` uses an isolated containerd image store. Importing the image using:

```bash
docker save cloud-native-app:v2.0 | docker exec -i desktop-control-plane ctr --namespace=k8s.io images import -
```

allows `imagePullPolicy: IfNotPresent` to resolve local images.

### 2. Host Port 5000 Conflict

Stopped and removed the standalone `cloud-app-container` before initiating:

```bash
kubectl port-forward svc/cloud-app-service 5000:5000
```

### 3. NodePort Network Isolation on Windows

Verified external browser access using `kubectl port-forward` and internal NodePort (`30005`) load distribution through an ephemeral in-cluster curl pod.

---

## ✅ Conclusion

This project demonstrates practical implementation of cloud-native application deployment using Docker and Kubernetes. It covers multi-stage image optimization, non-root container security, health monitoring, automated recovery, rolling updates, service discovery, load balancing, and horizontal scaling.

The implementation provides a foundation for deploying secure, scalable, and production-oriented containerized microservices.

---
