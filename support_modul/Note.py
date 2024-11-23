import flet as fl
from loguru import logger
import sqlite3 as sq
import sys

sys.path.append("..")
from support_modul.Color import Color



class Note(fl.Container):

    list_note = []
    def __init__(self, title, content, bgcolor="#407375", *args, **kwargs):
        super().__init__(
            height=200,
            width=200,
            padding=10,
            border_radius=10,
            border=fl.border.all(1, "black"),
            bgcolor=Color.color_user["notes"],
            content=fl.Column([
                fl.Text(title, size=18, italic=True, weight="bold"),
                fl.Text(content, overflow="clip")
            ],
                alignment="start",
                spacing=10
            ),
            alignment=fl.alignment.center
        )

    @classmethod
    def create_note(cls, user, page):
        logger.info("Creating a new note")

        # Генерация имени новой заметки
        if cls.list_note:
            name_previous_note = cls.list_note[-1][0]  # Берем имя последней заметки
            name_new_note = "Note_" + str(int(name_previous_note.split("_")[1]) + 1)
        else:
            name_new_note = "Note_1"

        # Создаем новую заметку
        logger.info("show page new note")
        new_note = cls.page_new_note(user, page, name_new_note)

    @classmethod
    def page_new_note(cls, user, page, name_new_note):
        logger.info("in page note")
        page.controls.clear()

        title = fl.TextField(label="Header", text_style=fl.TextStyle(color="black"), label_style=fl.TextStyle(color="black"))
        content = fl.TextField(label="Content",text_style=fl.TextStyle(color="black"),label_style=fl.TextStyle(color="black"), multiline=True)

        button_back = fl.IconButton(
            fl.icons.ARROW_BACK,
            icon_color=Color.color_user["button"],
            on_click=lambda e: cls.exiting_a_note(user, page, name_new_note, title, content)
        )

        # Правильное создание Row и Column
        page.add(fl.Column([
            fl.Row([button_back, title]),  # Создаём Row с элементами
            content  # Добавляем поле для контента
        ]))
        page.update()


    @classmethod
    def exiting_a_note(cls, user, page, name_new_note, title="", content=""):
        try:
            with sq.connect("BD/notes.db") as con:  # Исправил название базы на user_notes.db
                cur = con.cursor()
                # Исправляем запрос: убираем WHERE и добавляем user в VALUES
                cur.execute("INSERT INTO notes (user_name, name_note, title, content) VALUES (?, ?, ?, ?)",
                            (user, name_new_note, title.value, content.value))  # Используем title.value и content.value

            logger.info(f"Note '{name_new_note}' saved for user '{user}'")
        except Exception as e:
            logger.error(f"Error saving note: {e}")

        from main_page.Main_page import show_main_page
        show_main_page(user, page)

