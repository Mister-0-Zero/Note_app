import flet as fl, sqlite3 as sq
from main_page import show_main_page
from color import Color
from tables import create_tables, new_user, check_for_user_availability
from loguru import logger

logger.remove()
logger.add("debug.log", format = "{time} {level} {file} {line} {message}", mode = "w", level="DEBUG")


logger.catch()
def main(page: fl.Page):

    logger.info("Start programm")
    create_tables()
    user_name = check_for_user_availability()
    Color.color_user_m(user_name)

    # Главная страница с заметками
    show_main_page(user_name, page)

if __name__ == "__main__":
    fl.app(target=main)
