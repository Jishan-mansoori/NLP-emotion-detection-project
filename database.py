import sqlite3
from datetime import datetime

DB_NAME ="journal.db"

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT,
            emotion TEXT,
            timestamp TEXT
            )
            """)
    
    conn.commit()
    conn.close()
    
def insert_entry(text,emotion):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute(
        "INSERT INTO entries (text, emotion, timestamp) values (?,?,?)",
        (text, emotion , timestamp)
    )
    
    conn.commit()
    conn.close()
    
def get_entries():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("select * from entries order by id desc")
    
    rows = cursor.fetchall()
    
    conn.close()
    
    return rows