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

    # cria dimensão produto
    cur.execute("""
        CREATE TABLE IF NOT EXISTS dim_produto (
            produto_id INT PRIMARY KEY,
            nome TEXT,
            categoria TEXT,
            preco FLOAT,
            updated_at TIMESTAMP
        )
    """)

    # atualiza dados (modelo simples - truncate + insert)
    cur.execute("TRUNCATE TABLE dim_produto")

    cur.execute("""
        INSERT INTO dim_produto (produto_id, nome, categoria, preco, updated_at)
        SELECT
            id,
            title,
            category,
            price,
            collected_at
        FROM silver_products
    """)

    conn.commit()
    cur.close()
    conn.close()
