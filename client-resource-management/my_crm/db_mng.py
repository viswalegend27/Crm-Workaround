import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()  

conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST", "localhost"),
    port=os.getenv("DB_PORT", "5432"),
)
# my cursor object
cur = conn.cursor()
# Tyler123!
# executing my query
cur.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(100),
    salary INTEGER
);
""")

conn.commit()
cur.close()
conn.close()

print("Table created successfully ✅")
