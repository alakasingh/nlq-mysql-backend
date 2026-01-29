from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class TestPayload(BaseModel):
    name: str
    age: int

@router.post("/test")
def test_api(payload: TestPayload):
    return {
        "message": "Data received from router",
        "name": payload.name,
        "age": payload.age
    }

