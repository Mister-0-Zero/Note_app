import flet as fl
from AddElInt import Appbar
from color import Color
from note import Note

def show_main_page(user, page):
    page.controls.clear()

    page.bgcolor = Color.color_user["background"]

    # Добавляем AppBar на страничку
    Appbar(user, page)

    page.add(fl.FloatingActionButton(
        fl.icons.ADD,
        bgcolor = Color.color_user["button"],
        on_click=lambda e: Note.create_note(page)
    ))

