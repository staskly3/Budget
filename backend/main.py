import requests
import time
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Указываем адреса, которым разрешено делать запросы к бэкенду
origins = [
    "https://onrender.com",  # URL вашего будущего JS-фронтенда на Render
    "http://localhost:3000",                 # Локальный фронтенд для тестов
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Можно указать ["*"] для открытия API всему миру
    # allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/api/data")
def get_data():
    return {"status": "success", "message": "Привет от Python бэкенда!"}
