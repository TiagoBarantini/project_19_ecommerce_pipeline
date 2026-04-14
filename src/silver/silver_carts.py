import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def run():

    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        port=os.getenv("POSTGRES_PORT")
    )

    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS silver_carts AS
        SELECT DISTINCT ON (id, product_id)
            id,
            user_id,
            date,
            product_id,
            quantity,
            collected_at
        FROM bronze_carts
        ORDER BY id, product_id, collected_at DESC
    """)

    conn.commit()
    cur.close()
    conn.close()
