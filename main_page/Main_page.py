import flet as fl
from loguru import logger
import sqlite3 as sq
import sys

sys.path.append("..")
from main_page.AddElInt import *
from support_modul.Color import Color
from support_modul.Note import Note


def show_main_page(user, page):
    logger.info("Rendering the main page")

    page.controls.clear()

    page.bgcolor = Color.color_user["background"]

    Appbar(user, page)
    # Получаем список заметок из базы данных
    list_notes = []
    with sq.connect("BD/notes.db") as con:
        cur = con.cursor()
        list_notes = cur.execute("SELECT title, content FROM notes").fetchall()

    note_containers = []
    for title, content in list_notes:
        note_containers.append(
                Note(title, content, page)
        )

    page.add(
        fl.Stack(
            controls=[
                fl.Column(
                    controls=[
                        fl.ResponsiveRow(controls=note_containers),  # Ваши заметки
                    ],
                    scroll="adaptive",
                ),
                fl.Container(
                    DELETE(user, page),
                    alignment=fl.alignment.bottom_right,  # Фиксируем внизу справа
                    margin=fl.margin.only(right=16, bottom=16),
                ),
                fl.Container(
                    ADD(user, page),
                    alignment=fl.alignment.bottom_right,  # Чуть выше, но всё ещё справа
                    margin=fl.margin.only(right=16, bottom=80),
                ),
            ], expand=True,
        )
    )

    page.update()