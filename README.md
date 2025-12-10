# fastapi-sqlmodel-db-postgres-
Database models and connection setup for FastAPI using SQLModel and PostgreSQL

## 📁 Project Structure


<img width="800" height="500" alt="image" src="https://github.com/user-attachments/assets/d859f675-e342-4235-a3c8-7d23dea93369" />

## 🛠️ Prerequisites
Python 3.8+ <br>
PostgreSQL 12+ <br>
pip (Python package manager)<br>

# 📦 Installation & Setup
## 1. Clone and Setup Environment
```bash
# Create virtual environment
  python3 -m venv env

# Activate virtual environment
  - On Linux/Mac:
    source env/bin/activate

  - On Windows:
    env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 2: PostgreSQL Database Setup
```bash
-- Switch to postgres user
sudo -i -u postgres

-- Create database
CREATE DATABASE Library_db;

-- Create user and grant privileges
CREATE USER library_user WITH PASSWORD 'admin';
GRANT ALL PRIVILEGES ON DATABASE Library_db TO library_user;
GRANT USAGE, CREATE ON SCHEMA public TO library_user;
```
## 3: Initialize Database
```bash
# Run the database initialization script
  python create_db.py
```
## 4: Expected Output:
```bash
Tables created (if not existing).
```
