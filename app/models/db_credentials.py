from pydantic import BaseModel

class DBCredentials(BaseModel):
    host: str
    user: str
    password: str
    database: str

