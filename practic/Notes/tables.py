import sqlite3 as sq
from get_MAC_adress import get_mac_address
from color import Color

def new_user(mac_adr):
    with sq.connect("notes_users.db") as con:
        cur = con.cursor()
        user_count = cur.execute("SELECT COUNT(*) FROM users").fetchone()[0]
        user_name = f"user{user_count + 1}"
        cur.execute("INSERT INTO users (name, mac_adr) VALUES (?, ?)", (user_name, mac_adr))
        con.commit()
    return user_name

def create_tables():
    with sq.connect("notes_users.db") as con:
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE,
                mac_adr TEXT UNIQUE
            )
            """)


    with sq.connect("notes_color.db") as con:
        cur = con.cursor()
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


def check_for_user_availability():
    with sq.connect("notes_users.db") as con:
        cur = con.cursor()
        mac_adr = get_mac_address()
        if cur.execute("SELECT 1 FROM users WHERE mac_adr=?", (mac_adr,)).fetchone() is None:
            user_name = new_user(mac_adr)
            initialization_default_color(user_name)
        else:
            user_name = cur.execute("SELECT name FROM users WHERE mac_adr=?", (mac_adr,)).fetchone()[0]
    return user_name

def initialization_default_color(user_name):
    with sq.connect("notes_color.db") as con:
        cur = con.cursor()
        for element, value in Color.color_default.items():
            cur.execute("INSERT INTO color (user_name, element, value) VALUES (?,?,?)", (user_name, element, value))
        con.commit()
