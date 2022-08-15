import psycopg2
from config import DB_URL

conn = psycopg2.connect(DB_URL, sslmode="require")
cursor = conn.cursor()

"""DEF"""


async def save_db(user_id, text):
    postgres_insert_query = (
        """ INSERT INTO messages (id, telegram_id, text) VALUES (DEFAULT,%s,%s)"""
    )
    record_to_insert = (
        int(user_id),
        str(text),
    )
    cursor.execute(postgres_insert_query, record_to_insert)
    conn.commit()


async def read_db(user_id):
    results = await cursor.fetch_all(
        "SELECT text FROM messages WHERE telegram_id = :telegram_id ",
        values={"telegram_id": user_id},
    )
    return [next(result.values()) for result in results]


async def drop_db():
    sql = """
    DROP TABLE EMPLOYEE
    """
    cursor.execute(sql)
    conn.commit()


async def add_db():
    sql1 = """
    CREATE TABLE messages (
        id SERIAL PRIMARY KEY,
        telegram_id INTEGER NOT NULL,
        text text NOT NULL
    )
    """

    sql = """
    CREATE TABLE EMPLOYEE(
        FIRST_NAME CHAR(20) NOT NULL,
        LAST_NAME CHAR(20),
        AGE INT,
        SEX CHAR(1),
        INCOME FLOAT
    )"""
    cursor.execute(sql1)
    conn.commit()


"""DEF"""
