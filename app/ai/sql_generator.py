import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("API_KEY"))

def generate_sql(question: str, schema: dict) -> str:
    prompt = f"""
You are an expert MySQL SQL generator.

STRICT RULES:
- Use ONLY the tables and columns provided
- DO NOT hallucinate table or column names
- Generate only SELECT queries
- DO NOT modify data
- If LIMIT is missing, add LIMIT 100
- Return ONLY raw SQL, no explanation

DATABASE SCHEMA:
{schema}

USER QUESTION:
{question}
"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",   # ✅ FIXED MODEL
        contents=prompt
    )
    
    # ✅ SAFE EXTRACTION
    if not response or not getattr(response, "text", None):
        raise ValueError("AI returned empty response")

    sql = response.text.strip()

    if not sql.lower().startswith("select"):
        raise ValueError("Generated SQL is invalid")

    return sql
