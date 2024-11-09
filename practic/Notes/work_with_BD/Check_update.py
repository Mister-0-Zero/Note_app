import sqlite3 as sq
import sys

sys.path.append("..")
from support_modul.Color import Color

def check_update(user_name):
    check_setting_update(user_name)
    with sq.connect("BD/notes.db") as con:
        pass

def check_setting_update(user_name):
    with sq.connect("BD/notes.db") as con:
        cur = con.cursor()
        for element, value in Color.color_default.items():
            cur.execute("SELECT 1 FROM color WHERE user_name = ? AND element = ?", (user_name, element))
            exist = cur.fetchone()
            if not exist:
                cur.execute("INSERT INTO color (user_name, element, value) VALUES (?, ?, ?)", (user_name, element, value))
        con.commit()