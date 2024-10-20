import sqlite3 as sq

def check_update(user_name):
    check_setting_update(user_name)
    with sq.connect("../notes_color.db") as con:
        pass

def check_setting_update(user_name):
    pass