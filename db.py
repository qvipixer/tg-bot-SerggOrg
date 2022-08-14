"""
from databases import Database

from config import DB_URL

database = Database(DB_URL)

"""
import os
import psycopg2

database = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()