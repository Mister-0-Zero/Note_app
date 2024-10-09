import flet as fl
from loguru import logger
from color import Color

class Note(fl.Container):

    list_note = []
    def __init__(self, title, content, bgcolor="#407375", *args, **kwargs):
        super().__init__(
            height=200,
            width=200,
            padding=10,
            border_radius=10,
            border=fl.border.all(1, "black"),
            bgcolor=bgcolor,
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
        from main_page import show_main_page

        # Генерация имени новой заметки
        if cls.list_note:
            name_previous_note = cls.list_note[-1][0]  # Берем имя последней заметки
            name_new_note = "Note_" + str(int(name_previous_note.split("_")[1]) + 1)
        else:
            name_new_note = "Note_1"

        # Создаем новую заметку
        new_note = cls(title="New Note", content="-")

        # Добавляем новую заметку в список
        cls.list_note.append([name_new_note, new_note])

        # Обновляем главную страницу для отображения новой заметки
        show_main_page(user, page)

