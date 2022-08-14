"""
from databases import Database



database = Database(DB_URL)

"""
import os
import psycopg2
from config import DB_URL

conn = psycopg2.connect(DB_URL, sslmode='require')
cursor = conn.cursor()
