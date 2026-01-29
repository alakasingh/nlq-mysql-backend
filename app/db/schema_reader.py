from sqlalchemy import inspect

def read_schema(engine):
    inspector = inspect(engine)
    schema = {}

    tables = inspector.get_table_names()

    for table in tables:
        columns = inspector.get_columns(table)
        schema[table] = [
            {
                "column": col["name"],
                "type": str(col["type"])
            }
            for col in columns
        ]

    return schema
