from fastapi import APIRouter, HTTPException
from sqlalchemy import text

from app.db.connection import create_db_engine
from app.models.db_credentials import DBCredentials

from app.db.schema_reader import read_schema



router = APIRouter()

@router.post("/connect")
def connect_db(payload: DBCredentials):
    try:
        engine = create_db_engine(
            payload.host,
            payload.user,
            payload.password,
            payload.database
        )

        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))

        schema = read_schema(engine)

        return {
            "message": "Database connected successfully",
            "schema": schema
        }

    except Exception as e:
      print("DB ERROR:", e)
      raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    
