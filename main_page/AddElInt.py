import flet as fl
import sys
import sqlite3 as sq
from loguru import logger

sys.path.append("..")
from Setting.Setting import Setting
from support_modul.Color import Color
from support_modul.Note import Note

def Appbar(user, page):
    page.add(fl.AppBar(
        center_title=True,
        bgcolor=Color.color_user["appbar"],
        title=fl.Text("Notes", color=Color.color_user["text"]),
        actions=[
            fl.IconButton(
                fl.icons.SETTINGS,
                on_click=lambda e: Setting(user, page),
                icon_color=Color.color_user["button"]
            )
        ]
    ))
    page.update()

def ADD(user, page):
    ADD = fl.FloatingActionButton(
        icon=fl.icons.ADD,
        bgcolor=Color.color_user["button"],
        on_click=lambda e: Note.create_note(user, page),  # Обработка события добавления новой заметки
    )
    return ADD

def DELETE(user, page):
    DELETE = fl.FloatingActionButton(
        icon=fl.icons.DELETE,
        bgcolor=Color.color_user["button"],
        on_click=lambda e: delete_all_note(user, page),
    )
    return DELETE

def delete_all_note(user, page):
    with sq.connect("BD/notes.db") as con:
        cur = con.cursor()
        cur.execute("DELETE FROM notes WHERE user_name=?", (user,))
        con.commit()
        logger.info("Notes were deleted from database")

    # Перезагружаем главную страницу после удаления заметок
    from main_page.Main_page import show_main_page
    show_main_page(user, page)

