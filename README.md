# Activity 1: Containerization and Deployment of a Cloud-Native Application

Python Flask microservice, containerized with a multi-stage Docker build and deployed on Kubernetes.

## Endpoints
- `GET /` : Application metadata (`message`, `status`, `version`, `environment`, `served_by`)
- `GET /health` : Health check endpoint used by Docker `HEALTHCHECK` and Kubernetes liveness/readiness probes

## Project Files
| File | Purpose |
|---|---|
| `app.py` | Stateless Flask REST microservice |
| `requirements.txt` | Python dependencies (`flask==3.0.0`) |
| `Dockerfile` | Multi-stage, non-root runtime image with `HEALTHCHECK` |
| `.dockerignore` | Excludes non-runtime files from Docker build context |
| `deployment.yaml` | 2-replica Deployment with RollingUpdate, resource limits, and health probes |
| `service.yaml` | NodePort Service (`30005`) exposing port `5000` |

## Run with Docker
```bash
docker build -t cloud-native-app:v2.0 .
docker run -d -p 5000:5000 --name cloud-app-container cloud-native-app:v2.0