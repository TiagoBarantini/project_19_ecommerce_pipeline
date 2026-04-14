import requests
import psycopg2
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def extract():
    url = "https://fakestoreapi.com/products"
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
        CREATE TABLE IF NOT EXISTS bronze_products (
            id INT,
            title TEXT,
            price FLOAT,
            category TEXT,
            collected_at TIMESTAMP
        )
    """)

    for item in data:
        cur.execute("""
            INSERT INTO bronze_products (id, title, price, category, collected_at)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            item['id'],
            item['title'],
            item['price'],
            item['category'],
            datetime.now()
        ))

    conn.commit()
    cur.close()
    conn.close()

def run():
    data = extract()
    load(data)
