import sys
sys.path.append("..")

from Setting.setting_color import *
from Setting.State_set import SettingState


state = SettingState()
# Переменная для отслеживания состояния отображения элементов
is_color_setting_visible = False

logger.catch()
def Setting(user, page, dropdown_val=None, color_val="#000000"):
    logger.info("Rendering a page of setting")

    # Очищаем содержимое страницы
    page.controls.clear()

    # AppBar с иконкой возврата
    create_object_setting(user, page, dropdown_val, color_val)

    # Обновляем страницу
    page.update()

def create_object_setting(user, page, dropdown_val, color_val):
    from Main_page import show_main_page

    # Создаем AppBar
    page.appbar = fl.AppBar(
        center_title=True,
        bgcolor=Color.color_user["appbar"],
        title=fl.Text("Setting", color=Color.color_user["text"]),
        leading=fl.IconButton(
            fl.icons.ARROW_BACK,
            icon_color=Color.color_user["button"],
            on_click=lambda e: show_main_page(user, page)
        )
    )


    # Текст с событием нажатия, который будет отображать настройки цвета
    color_set_text = fl.GestureDetector(
        content=fl.Text("-Color setting:", color=Color.color_user["text"], size=20),
        on_tap=lambda e: toggle_color_setting(user, page, dropdown_val, color_val, state)
    )

    # Добавляем `color_set_text` и `container` в иерархию страницы
    page.add(fl.Column([color_set_text, state.container]))
    logger.info(f"Conteiner: {state.container}")

    # Обновляем страницу, чтобы Flet применил изменения
    page.update()

