import flet as fl
from AddElInt import Appbar

def show_main_page(page):
    page.controls.clear()

    # Добавляем AppBar на страничку
    Appbar(page)