import flet as fl
from AddElInt import Appbar
from color import Color
from note import Note
from loguru import logger

def show_main_page(user, page):
    logger.info("Rendering the main page")
    page.controls.clear()

    page.bgcolor = Color.color_user["background"]

    # Добавляем AppBar на страничку
    Appbar(user, page)

    # Кнопка добавления новой заметки
    page.add(fl.FloatingActionButton(
        icon=fl.icons.ADD,
        bgcolor=Color.color_user["button"],
        on_click=lambda e: Note.create_note(user, page)
    ))

    # Рендер всех заметок из списка
    page.add(fl.ResponsiveRow(
        controls=[
            fl.Container(note, col={"xs": 12, "sm": 6, "md": 4, "lg": 3, "xl": 2})
            for name_note, note in Note.list_note  # Извлечение заметок из списка
        ]
    ))

    page.update()  # Обновляем страницу
