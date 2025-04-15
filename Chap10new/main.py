# main.py
from fastapi import FastAPI
from database import Base, engine
from routers import book_router,auth_router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)
Base.metadata.create_all(bind=engine)
app.include_router(book_router.router)
app.include_router(auth_router.router, prefix="/api/v1")
