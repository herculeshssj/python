from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Defina quais origens podem acessar sua API
origins = [
    "http://localhost:5173",  # frontend Vue
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/items")
def get_items():
    return {"items": ["Banana", "Maçã", "Laranja"]}
