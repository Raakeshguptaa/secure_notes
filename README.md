# 🛡️ Secure Notes API – FastAPI + OAuth2 + JWT

A simple, secure Notes REST API built with **FastAPI**, **OAuth2 Password Flow**, **JWT authentication**, and **SQLAlchemy ORM**.

Users can register, log in, and manage personal notes securely using token-based authentication. Test it easily with Postman!

---

## 🔧 Features

- ✅ User Registration
- 🔐 Login with OAuth2 (Password flow)
- 🔑 JWT Access Token generation
- 🔒 Protected endpoints using Bearer tokens
- 📝 Create, Read, and View Notes (only your own!)
- 🧪 Postman-ready API for testing
- 🗃️ SQLAlchemy-based database modeling (SQLite / PostgreSQL ready)

---

## 📁 Project Structure

📦 secure-notes-api
├── main.py # Main FastAPI app with routes and logic
├── models.py # SQLAlchemy models (User, Note)
├── schemas.py # Pydantic schemas (User input/output)
├── database.py # DB setup and session management
├── requirements.txt # Python dependencies
└── README.md # This file 

## 🚀 Getting Started

### 1. Clone the Repo

bash
git clone https://github.com/your-username/secure-notes-api.git
cd secure-notes-api

### 2. Install Dependencies

bash
pip install -r requirements.txt

### 3.Run the API
uvicorn main:app --reload


🔐 Authentication Flow
Users register using /user

Login using /login (OAuth2 password flow)

Receive a JWT token

Use the token in the Authorization header as:
Authorization: Bearer <your_token_here>

🔐 Auth & User
Method	Endpoint	Description
POST	/user	Register new user
POST	/login	Login and get token

📝 Notes
Method	Endpoint	Description
GET	/note_detail	View all notes (auth only)
GET	/notes/{note_id}	View a specific note
POST	/note	Add new note (auth o
