import flet as fl
from Main_page import show_main_page
from Color import Color
from work_with_BD.Tables import create_tables, check_for_user_availability
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
