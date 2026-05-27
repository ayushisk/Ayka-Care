📝 Notes Management API (FastAPI)

A simple Notes Management REST API built using FastAPI, SQLAlchemy, and JWT Authentication.
This project allows users to register, login, and perform full CRUD operations on personal notes.

🚀 Tech Stack
Python 3.10+
FastAPI
SQLite (can be replaced with PostgreSQL/MySQL)
SQLAlchemy ORM
Pydantic
JWT (JSON Web Token)
Passlib (bcrypt hashing)

📌 Features

🔐 Authentication

User Registration API
User Login API
JWT Token-based Authentication
🗒 Notes Management
Create Note
Get All Notes (User-specific)
Update Note
Delete Note

📂 Project Structures

app/
│
├── main.py # FastAPI routes
├── models.py # Database models
├── schemas.py # Pydantic schemas
├── database.py # DB connection setup
├── auth.py # Authentication & JWT logic
│
notes.db # SQLite database (auto-created)
⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/your-username/notes-api.git
cd notes-api
2️⃣ Create Virtual Environment
python -m venv venv
Activate venv

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate
3️⃣ Install Dependencies
pip install fastapi uvicorn sqlalchemy passlib bcrypt python-jose pydantic
4️⃣ Run the Server
uvicorn app.main:app --reload
🌐 API Base URL
http://localhost:8000
📘 API Documentation (Swagger UI)

FastAPI automatically provides interactive docs:

Swagger UI 👉 http://localhost:8000/docs
ReDoc 👉 http://localhost:8000/redoc
🔐 Authentication Flow

1. Register User

POST /register

{
"email": "test@gmail.com",
"password": "123456"
} 2. Login User

POST /login

{
"email": "test@gmail.com",
"password": "123456"
}
Response:
{
"access_token": "jwt_token_here",
"token_type": "bearer"
} 3. Use Token in Protected Routes

Add this in headers:

Authorization: Bearer <your_token>
🗒 Notes APIs
➕ Create Note

POST /notes

{
"title": "My Note",
"content": "This is my note content"
}
📄 Get All Notes

GET /notes

✏️ Update Note

PUT /notes/{note_id}

{
"title": "Updated Title",
"content": "Updated content"
}
❌ Delete Note

DELETE /notes/{note_id}

🧪 Testing (Postman)

You can test APIs using:

Postman Collection (recommended)
Swagger UI (/docs)
⚠️ Error Handling
400 → Email already registered
401 → Invalid credentials / Unauthorized access
404 → Note not found
500 → Server error
🎯 Bonus Features Implemented
JWT Authentication 🔐
Password hashing using bcrypt 🔑
User-specific notes isolation 👤
Swagger documentation 📘
🚀 Future Improvements
Add pagination for notes
Role-based access (Admin/User)
Deploy using Docker
Deploy on Render / AWS / Railway
Add refresh tokens

👨‍💻 Author

Ayushi Sinha
Built as part of FastAPI backend assignment.
