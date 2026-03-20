import mysql.connector

import sqlite3

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",   # your password
        database="dryfruit_store"
    )


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn