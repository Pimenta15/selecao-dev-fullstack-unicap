from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router

app = FastAPI(title="Text-to-Image API", version="1.0")

# Configurar CORS (para o front conseguir acessar)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # em produção, restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
