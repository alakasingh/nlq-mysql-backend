from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.ai.sql_generator import generate_sql
from app.db.sql_validator import validate_sql
from app.db.sql_executor import execute_sql
from app.db.connection import create_db_engine

router = APIRouter()

class NLQRequest(BaseModel):
    question: str
    db_schema: dict
    db_credentials: dict

@router.post("/query")
def nl_query(payload: NLQRequest):
    try:
        engine = create_db_engine(
            payload.db_credentials["host"],
            payload.db_credentials["user"],
            payload.db_credentials["password"],
            payload.db_credentials["database"]
        )

        sql = generate_sql(payload.question, payload.db_schema)
        validate_sql(sql)
        results = execute_sql(engine, sql)

        return {
            "sql": sql,
            "results": results
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        print("DB ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))

        
    
