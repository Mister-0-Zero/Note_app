from loguru import logger
import sys
sys.path.append("..")
from Get_MAC_adress import get_mac_address
from Color import Color
import sqlite3 as sq
from work_with_BD.Initialization_user import initialization_user
from work_with_BD.Check_update import check_update

def create_tables():
    with sq.connect("BD/notes.db") as con:
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE,
                mac_adr TEXT UNIQUE
            )
            """)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS color (
            record_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT,
            element TEXT,
            value TEXT,
            UNIQUE(user_name, element),
            FOREIGN KEY (user_name) REFERENCES  users(user_name) 
        )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_name TEXT,
                name_note TEXT,
                title TEXT,
                content TEXT,
                FOREIGN KEY (user_name) REFERENCES users(user_name)
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_name TEXT,
                picture_background INT,
                FOREIGN KEY (user_name) REFERENCES users(user_name)
            )
        """)

def check_for_user_availability():
    with sq.connect("BD/notes.db") as con:
        cur = con.cursor()
        mac_adr = get_mac_address()
        if cur.execute("SELECT 1 FROM users WHERE mac_adr=?", (mac_adr,)).fetchone() is None:
            user_name = new_user(mac_adr)
            initialization_user(user_name)
        else:
            user_name = cur.execute("SELECT name FROM users WHERE mac_adr=?", (mac_adr,)).fetchone()[0]
            check_update(user_name)
    return user_name

def new_user(mac_adr):
    with sq.connect("BD/notes.db") as con:
        cur = con.cursor()
        user_count = cur.execute("SELECT COUNT(*) FROM users").fetchone()[0]
        user_name = f"user{user_count + 1}"
        cur.execute("INSERT INTO users (name, mac_adr) VALUES (?, ?)", (user_name, mac_adr))
        con.commit()
    return user_name