# 🚀 AI Transfer Assistant  
### Routing + Decision Intelligence System for Multi-Platform Navigation

---

## 🧠 Overview

AI Transfer Assistant is an intelligent backend system that computes optimal navigation routes across transport platforms and evaluates transfer feasibility in real time.

It combines:
- Graph-based routing
- Accessibility-aware navigation
- Delay-aware decision logic
- Automation workflows (n8n)
- AI integration via MCP (Model Context Protocol)

---

## 🎯 Features

### 🔹 Smart Routing Engine
- Computes shortest path using graph algorithms
- Supports multiple modes:
  - fastest
  - no_stairs
  - wheelchair

---

### 🔹 Human-Readable Instructions
- Converts raw graph paths into step-by-step navigation guidance

---

### 🔹 Transfer Risk Evaluation
- Classifies transfers as:
  - Safe
  - Risky
  - Missed  

Based on:
- transfer time  
- delay  
- required route time  

---

### 🔹 Automation (n8n)
- Webhook-triggered workflows
- Real-time decision making
- Conditional logic

---

### 🔹 AI Integration (MCP)
- Exposes routing as tools:
  - find_route
  - list_nodes

---

## 🏗️ Architecture

User → n8n → FastAPI → Routing Engine → Response

---

## ⚙️ Tech Stack

- FastAPI (Python)
- n8n
- MCP
- Graph Algorithms

---

## 📡 API Endpoints

POST /route  
POST /transfer-check

---

## 🛠️ Setup

```bash
git clone https://github.com/JabranMustafa/ai-transfer-assistant.git
cd ai-transfer-assistant
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python run_server.py
```

---

## 🎥 Project Demo Video

The project demo video is available in the **Releases/Tags** section of this repository.

### How to Download

1. Click on **Releases** (or **Tags**) at the right side of this repository.
2. Open the latest release (`v1.0.0`).
3. Under **Assets**, download **demo.mp4**.
4. Watch the complete project demonstration.

> 📹 The demo video showcases the application's features, workflow, and user interface.

## 👤 Author

Jabran Mustafa  
