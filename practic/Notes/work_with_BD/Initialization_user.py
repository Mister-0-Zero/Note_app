import sqlite3 as sq
import sys

sys.path.append("..")
from support_modul.Color import Color

def initialization_user(user_name):
    initialization_color(user_name)
    initialization_data(user_name)

def initialization_color(user_name):
    with sq.connect("BD/notes.db") as con:
        cur = con.cursor()
        for element, value in Color.color_default.items():
            cur.execute("INSERT INTO color (user_name, element, value) VALUES (?,?,?)", (user_name, element, value))
        con.commit()

def initialization_data(user_name):
    pass