import requests
import psycopg2
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def extract():
    url = "https://fakestoreapi.com/carts"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def load(data):
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        port=os.getenv("POSTGRES_PORT")
    )

    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS bronze_carts (
            id INT,
            user_id INT,
            date TIMESTAMP,
            product_id INT,
            quantity INT,
            collected_at TIMESTAMP
        )
    """)

    for cart in data:
        for item in cart['products']:
            cur.execute("""
                INSERT INTO bronze_carts (id, user_id, date, product_id, quantity, collected_at)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                cart['id'],
                cart['userId'],
                cart['date'],
                item['productId'],
                item['quantity'],
                datetime.now()
            ))

    conn.commit()
    cur.close()
    conn.close()

def run():
    data = extract()
    load(data)
