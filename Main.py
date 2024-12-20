import flet as fl
from loguru import logger

from main_page.Main_page import show_main_page
from support_modul.Color import Color
from work_with_BD.Tables import create_tables, check_for_user_availability


logger.remove()
logger.add("debug.log", format = "{time} {level} {file} {line} {message}", mode = "w", level="DEBUG")


logger.catch()
def main(page: fl.Page):
    page.window_width = 1900  # Ширина окна
    page.window_height = 1100  # Высота окна

    logger.info("Start programm")
    create_tables()
    user_name = check_for_user_availability()
    Color.color_user_m(user_name)

    # Главная страница с заметками
    show_main_page(user_name, page)

if __name__ == "__main__":
    fl.app(target=main)
