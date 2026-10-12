# Expense Tracker API

Backend REST API for tracking personal expenses, built with FastAPI and SQLAlchemy.

## Tech stack
Python, FastAPI, SQLAlchemy, SQLite (PostgreSQL planned), Uvicorn

## Run locally
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    uvicorn app.main:app --reload

Then open http://127.0.0.1:8000/docs

## Project structure
    app/
      database.py   # database connection and session
      models.py     # User and Expense tables
      main.py       # FastAPI app and endpoints

## Status
In progress: models and health endpoint done. Next: expense CRUD, JWT auth, tests.