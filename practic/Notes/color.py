import sqlite3 as sq

class Color:
    color_default = {
        "background": "#407375",
        "appbar_notes": "#ffffff",
        "appbar_setting": "#ffffff",
        "button": "#000000",
        "notes": "#407375",
        "text": "#000000"
    }

    color_user = {}
    @classmethod
    def color_user_m(cls, user_name):
        with sq.connect("notes_color.db") as con:
            cur = con.cursor()
            cur.execute("SELECT element, value FROM color WHERE user_name=?", (user_name,))
            for element, value in cur.fetchall():
                cls.color_user[element] = value
            print(cls.color_user)

    @classmethod
    def change_color(cls, user_name, element, value):
        with sq.connect("notes_color.db") as con:
            cur = con.cursor()
            cur.execute("UPDATE color SET value = ? WHERE user_name = ? and element = ?", (value, user_name, element))
            cls.color_user[element] = value
            con.commit()


