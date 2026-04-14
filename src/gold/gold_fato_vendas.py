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
        CREATE TABLE IF NOT EXISTS fato_vendas (
            venda_id SERIAL PRIMARY KEY,
            produto_id INT,
            quantidade INT,
            data_venda TIMESTAMP
        )
    """)

    cur.execute("TRUNCATE TABLE fato_vendas")

    cur.execute("""
        INSERT INTO fato_vendas (produto_id, quantidade, data_venda)
        SELECT
            product_id,
            quantity,
            date
        FROM silver_carts
    """)

    conn.commit()
    cur.close()
    conn.close()
