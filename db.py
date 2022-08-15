"""
from databases import Database



database = Database(DB_URL)

"""
import os
import psycopg2
from config import DB_URL

conn = psycopg2.connect(DB_URL, sslmode='require')
cursor = conn.cursor()


async def save(user_id, text):
    postgres_insert_query = (
        """ INSERT INTO messages (id, telegram_id, text) VALUES (DEFAULT,%s,%s)"""
    )
    record_to_insert = (
        int(user_id),
        str(text),
    )
    cursor.execute(postgres_insert_query, record_to_insert)
    conn.commit()


async def read(user_id):
    results = await cursor.fetch_all(
        "SELECT text FROM messages WHERE telegram_id = :telegram_id ",
        values={"telegram_id": user_id},
    )
    return [next(result.values()) for result in results]