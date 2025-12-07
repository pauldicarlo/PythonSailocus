'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: https://github.com/pauldicarlo
'''

import sqlite3
from pathlib import Path

class Session:
    def __init__(self, db_connection:  sqlite3.Connection):
        self.db_Connection = db_connection

def createSession() -> Session:
    db_path = Path("sailocus.db")


    if db_path.exists():
        print(f"Opening existing database: {db_path}")
        db_new = False
    else:
        print(f"Creating new database: {db_path}")
        db_new = True

    try:
        # Connect to db file or create
        conn = sqlite3.connect(db_path)
        # create a connection just to be sure

        if db_new:
            create_tables(conn)
        print("Database connection established.")
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")

    session = Session(conn)
    return session 


def create_tables(conn: sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        id TEXT NOT NULL,
        password_hash TEXT NOT NULL
    )
    ''')
    conn.commit()
    pass