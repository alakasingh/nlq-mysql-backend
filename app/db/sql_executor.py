from sqlalchemy import text

def execute_sql(engine, sql_query):
    with engine.connect() as conn:
        result = conn.execute(text(sql_query))
        columns = list(result.keys())
        rows = result.fetchall()

        data = [dict(zip(columns, row)) for row in rows]

        return {
            "columns": columns,
            "data": data,
            "row_count": len(data)
        }
