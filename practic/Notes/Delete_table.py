import sqlite3 as sq

def drop_tables():
    with sq.connect("notes_users.db") as con:
        cur = con.cursor()
        # Удаление таблицы users, если она существует
        cur.execute("DROP TABLE IF EXISTS users")
        con.commit()

    with sq.connect("notes_color.db") as con:
        cur = con.cursor()
        # Удаление таблицы color, если она существует
        cur.execute("DROP TABLE IF EXISTS color")
        con.commit()

drop_tables()