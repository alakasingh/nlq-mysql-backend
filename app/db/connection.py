from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError


def create_db_engine(host, user, password, database, port=26656):
    try:
        url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        engine = create_engine(url)
        return engine
    except SQLAlchemyError as e:
        raise Exception("Database connection failed")

