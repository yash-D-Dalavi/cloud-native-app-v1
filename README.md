# Activity 1: Containerization and Deployment of a Cloud-Native Application

## 1. Project Overview

This project demonstrates the end-to-end containerization and deployment of a lightweight cloud-native Python Flask application using Docker and Kubernetes.

The main objective of this activity is to understand how applications can be packaged into Docker containers and deployed, managed, and exposed using Kubernetes orchestration.

The project includes:
- Development of a Python Flask web application.
- Creation of a custom Docker image using a Dockerfile.
- Building and running Docker containers.
- Deployment of the application using Kubernetes.
- Configuration of Kubernetes Deployment with 2 replicas.
- Exposure of the application using a NodePort Service.
- Testing application endpoints and verifying deployment status.

## 2. Objectives

- To understand the fundamentals of containerization.
- To create a Docker image for a Python Flask application.
- To execute and manage Docker containers.
- To understand Kubernetes architecture and orchestration.
- To deploy an application using Kubernetes Deployment.
- To configure multiple pod replicas for application availability.
- To expose the application using Kubernetes NodePort Service.
- To verify application accessibility and health status.

## 3. Technology Stack and Prerequisites

| Technology | Purpose |
|---|---|
| Python 3.9 | Application Development |
| Flask | Python Web Framework |
| Docker Desktop | Containerization |
| Dockerfile | Docker Image Configuration |
| Kubernetes | Container Orchestration |
| kubectl | Kubernetes Command-Line Tool |
| Git | Version Control |
| GitHub | Source Code Repository |

### Prerequisites

Before executing this project, ensure that the following tools are installed:

1. Python 3.9 or later.
2. Docker Desktop.
3. Kubernetes enabled in Docker Desktop.
4. kubectl command-line tool.
5. Git and GitHub account.
6. A code editor such as Visual Studio Code.

## 4. Repository Structure

The project repository contains the following files:

```text
cloud-native-app-v1/
│
├── app.py              # Flask Web Application Source Code
├── requirements.txt    # Python Dependencies
├── Dockerfile          # Docker Image Configuration
├── deployment.yaml     # Kubernetes Deployment (2 Replicas)
├── service.yaml        # Kubernetes NodePort Service
└── README.md           # Project Documentation
```

### File Description

- **app.py:** Contains the Python Flask application and REST API endpoints.
- **requirements.txt:** Specifies the Python libraries required to run the application.
- **Dockerfile:** Defines the instructions for building the Docker image.
- **deployment.yaml:** Defines the Kubernetes Deployment configuration with two pod replicas.
- **service.yaml:** Exposes the application externally using a NodePort Service.
- **README.md:** Provides project information and execution instructions.

## 5. Implementation and Execution Steps

### Step 1: Clone the Repository

Clone the project repository to your local system.

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Navigate to the project directory:

```bash
cd cloud-native-app-v1
```

### Step 2: Build the Docker Image

Build a custom Docker image using the Dockerfile.

```bash
docker build -t cloud-native-app:v1.0 .
```

This command builds the application image and tags it as `cloud-native-app:v1.0`.

### Step 3: Run the Docker Container

Execute the Docker container and map port 5000 of the host machine to port 5000 of the container.

```bash
docker run -d -p 5000:5000 --name cloud-app-container cloud-native-app:v1.0
```

### Step 4: Verify the Docker Container

Check whether the container is running successfully.

```bash
docker ps
```

To view container logs:

```bash
docker logs cloud-app-container
```

Open the application in a web browser:

```text
http://localhost:5000
```

### Step 5: Verify Kubernetes Availability

Ensure that Kubernetes is enabled in Docker Desktop.

Check the Kubernetes cluster status:

```bash
kubectl cluster-info
```

Check the available nodes:

```bash
kubectl get nodes
```

### Step 6: Deploy the Application Using Kubernetes

Apply the Kubernetes Deployment manifest.

```bash
kubectl apply -f deployment.yaml
```

The deployment creates two application pod replicas as configured in the manifest.

### Step 7: Expose the Application Using NodePort Service

Apply the Kubernetes Service manifest.

```bash
kubectl apply -f service.yaml
```

The NodePort Service provides access to the application through the configured service port.

### Step 8: Verify Kubernetes Deployment

Check the running pods:

```bash
kubectl get pods
```

Check the deployment status:

```bash
kubectl get deployments
```

Check the available services:

```bash
kubectl get services
```

Check detailed deployment information:

```bash
kubectl describe deployment
```

### Step 9: Access the Application

To access the application locally using Kubernetes port forwarding, execute:

```bash
kubectl port-forward svc/cloud-app-service 5000:5000
```

Open the following URL in your browser:

**Application URL:**

```text
http://localhost:5000/
```

**Health Check URL:**

```text
http://localhost:5000/health
```

If the application is configured correctly, both endpoints should return their expected responses.

## 6. REST API Endpoints

The Flask application provides the following REST API endpoints:

| Endpoint | HTTP Method | Description |
|---|---|---|
| `/` | GET | Returns application status and JSON metadata. |
| `/health` | GET | Returns HTTP 200 OK to indicate application health. |

### Endpoint Testing

**1. Root Endpoint**

```text
http://localhost:5000/
```

Purpose: Verifies that the main Flask application is accessible.

**2. Health Endpoint**

```text
http://localhost:5000/health
```

Purpose: Checks whether the application is running and responding correctly.

## 7. Docker Commands Reference

| Command | Description |
|---|---|
| `docker build -t cloud-native-app:v1.0 .` | Builds the Docker image. |
| `docker images` | Lists available Docker images. |
| `docker run -d -p 5000:5000 --name cloud-app-container cloud-native-app:v1.0` | Runs the Docker container. |
| `docker ps` | Displays running containers. |
| `docker logs cloud-app-container` | Displays container logs. |
| `docker stop cloud-app-container` | Stops the running container. |
| `docker rm cloud-app-container` | Removes the container. |

## 8. Kubernetes Commands Reference

| Command | Description |
|---|---|
| `kubectl cluster-info` | Displays Kubernetes cluster information. |
| `kubectl get nodes` | Displays available cluster nodes. |
| `kubectl apply -f deployment.yaml` | Creates or updates the deployment. |
| `kubectl apply -f service.yaml` | Creates or updates the service. |
| `kubectl get pods` | Displays running pods. |
| `kubectl get deployments` | Displays deployments. |
| `kubectl get svc` | Displays Kubernetes services. |
| `kubectl describe deployment` | Displays deployment details. |
| `kubectl port-forward svc/cloud-app-service 5000:5000` | Forwards local traffic to the Kubernetes service. |
| `kubectl delete -f service.yaml` | Deletes the service. |
| `kubectl delete -f deployment.yaml` | Deletes the deployment. |

## 9. Expected Results

After successfully completing all the implementation steps, the following results are expected:

1. The Docker image should be built successfully.
2. The Docker container should start and run without errors.
3. The Flask application should be accessible through the browser.
4. Kubernetes should successfully create the application deployment.
5. Two application pod replicas should reach the Running state.
6. The NodePort Service should be created successfully.
7. The application should respond through the Kubernetes service.
8. The `/health` endpoint should return HTTP 200 OK.

## 10. Learning Outcomes

Through this activity, the following concepts were learned:

- Understanding containerization and its importance in modern application development.
- Building and managing Docker images and containers.
- Understanding Docker networking and port mapping.
- Learning Kubernetes Deployment and Pod management.
- Understanding the importance of replicas in application availability.
- Configuring Kubernetes Services for application exposure.
- Executing application deployment and verification using kubectl.
- Understanding the fundamentals of cloud-native application deployment.

## 11. Conclusion

This activity successfully demonstrates the containerization and Kubernetes deployment workflow for a Python Flask cloud-native application.

Docker was used to package the application into a portable container image, while Kubernetes was used to deploy and manage the application with two replicas. A NodePort Service was configured to expose the application, and the REST API endpoints were used to verify its functionality.

Overall, this activity provided practical knowledge of Docker containerization, Kubernetes orchestration, application deployment, service exposure, and cloud-native technologies.

---

**Project:** Containerization and Deployment of a Cloud-Native Application  
**Activity:** Activity 1  
**Technologies:** Python, Flask, Docker, Kubernetes, Git and GitHub
