# 🧑‍⚕️ Cluster ER

> A Python-based DevOps tool to diagnose Kubernetes clusters and capture incident data in seconds.

---

## 🚀 Overview

Cluster ER is a production-style DevOps CLI tool designed to help engineers quickly identify issues in Kubernetes clusters and collect critical debugging information during incidents.

Instead of manually running multiple `kubectl` commands, this tool automates health checks and incident data collection into a single workflow.

---

## ⚡ Features

### 🔍 Cluster Health Checks
- Detect NotReady nodes  
- Identify problematic pods:
  - CrashLoopBackOff  
  - ImagePullBackOff  
  - Failed pods  

### 📸 Incident Capture
- Collects:
  - All cluster resources  
  - Kubernetes events  
  - Logs from failing pods  

### 📦 Debug Bundle
- Compresses all collected data into a single archive:
        incident_<timestamp>.tar.gz

---

## 🛠️ Tech Stack

- Python  
- Kubernetes (kubectl)  
- Minikube (for local testing)  

---

## 📂 Project Structure
cluster-doctor/
│
├── main.py
├── checks/
│ ├── nodes.py
│ ├── pods.py
│ └── incidents.py
│
├── utils/
│ └── kubectl.py
│
└── README.md


---

## ▶️ How It Works

```text
Run tool → Check cluster health → Detect issues → Capture data → Compress → Done

⚙️ Usage
1. Start your Kubernetes cluster (Minikube)
minikube start
2. Run the tool
python main.py
🧪 Example Output
=== Cluster Doctor ===

✅ All nodes are Ready

🔥 CrashLoopBackOff Pods: 1
 - default/badpod

📸 Capturing incident snapshot...
📦 Incident archive ready: incident_2026-03-28_14-30-00.tar.gz
