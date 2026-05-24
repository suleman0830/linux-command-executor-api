# Linux Command Executor API

## 📌 Project Overview

This project is a FastAPI-based backend application that executes predefined Linux system commands and returns their output in JSON format.

The purpose of this project is to practice:
- FastAPI
- Linux commands
- Python subprocess module
- API development
- Error handling
- Git & GitHub workflow

---

## 🚀 Features

- Execute predefined Linux commands securely
- JSON API responses
- Error handling implementation
- Health check endpoint
- Structured project architecture

---

## 🛠 Technologies Used

- Python
- FastAPI
- Uvicorn
- Linux Commands
- Git & GitHub

---

## 📂 Project Structure

```text
project/
│
├── main.py
├── routes/
├── utils/
├── requirements.txt
└── README.md
```

---

## 📌 API Endpoints

### Health Check
```http
GET /health
```

Response:

```json
{
  "status": "healthy"
}
```

---

### System Uptime
```http
GET /system/uptime
```

---

### Disk Usage
```http
GET /system/disk
```

---

### Memory Usage
```http
GET /system/memory
```

---

### Current User
```http
GET /system/whoami
```

---

## ▶️ Run Project

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run FastAPI server

```bash
uvicorn main:app --reload
```

---

## 🔒 Security Note

This project only allows predefined Linux commands.

Dynamic/custom command execution is intentionally restricted for security reasons.

---

## 👨‍💻 Author

Suleman