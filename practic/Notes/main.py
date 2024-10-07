from note import Note
from main_page import show_main_page
import flet as fl

def main(page: fl.Page):
    # Переменная для хранения выбранного цвета фона
    background_color = "#407375"

    # Список для хранения всех заметок
    notes = []

    # Главная страница с заметками
    show_main_page(page)

if __name__ == "__main__":
    fl.app(target=main)
