import re

FORBIDDEN_KEYWORDS = [
    "INSERT", "UPDATE", "DELETE",
    "DROP", "ALTER", "TRUNCATE",
    "CREATE", "REPLACE"
]

def validate_sql(sql: str):
    sql_upper = sql.upper()

    if not sql_upper.strip().startswith("SELECT"):
        raise ValueError("Only SELECT queries are allowed")

    for keyword in FORBIDDEN_KEYWORDS:
        if keyword in sql_upper:
            raise ValueError(f"Forbidden keyword detected: {keyword}")

    if not re.search(r"\bFROM\b", sql_upper):
        raise ValueError("Invalid SQL: missing FROM clause")

    return True
