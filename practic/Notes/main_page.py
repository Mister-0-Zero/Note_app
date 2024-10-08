import flet as fl
from AddElInt import Appbar
from color import Color

def show_main_page(user, page):
    page.controls.clear()

    page.bgcolor = Color.color_user["background"]

    # Добавляем AppBar на страничку
    Appbar(user, page)