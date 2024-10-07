import flet as fl
from main_page import show_main_page
from color import Color


def main(page: fl.Page):
    # Переменная для хранения выбранного цвета фона
    background_color = Color.background

    # Список для хранения всех заметок
    notes = []

    # Главная страница с заметками
    show_main_page(page)

if __name__ == "__main__":
    fl.app(target=main)
