from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.test import router as test_router
from dotenv import load_dotenv
import os
from routes.connect import router as connect_router
from routes.query import router as query_router


load_dotenv()
app = FastAPI(
     title=os.getenv("APP_NAME")
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers with /api prefix to match frontend
app.include_router(connect_router, prefix="/api")
app.include_router(test_router, prefix="/api")
app.include_router(query_router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Backend running with routers"}


