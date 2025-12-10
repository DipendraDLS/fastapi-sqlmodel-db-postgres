# fastapi-sqlmodel-db-postgres-
Database models and connection setup for FastAPI using SQLModel and PostgreSQL

## 📁 Project Structure
library-management/
│
├── core/
│   ├── __init__.py
│   ├── db.py              # Database connection and session management
│   └── config.py          # Application configuration
│
├── model/
│   ├── __init__.py
│   └── models.py          # SQLModel data models (Book, Students)
│
├── requirements.txt       # Python dependencies
├── create_db.py          # Database initialization script
├── .env                  # Environment variables (create this)
├── .gitignore
└── README.md
