import sqlite3 as sq
import sys
sys.path.append("..")
from Color import Color

def initialization_user(user_name):
    initialization_color(user_name)

def initialization_color(user_name):
    with sq.connect("../notes_color.db") as con:
        cur = con.cursor()
        for element, value in Color.color_default.items():
            cur.execute("INSERT INTO color (user_name, element, value) VALUES (?,?,?)", (user_name, element, value))
        con.commit()