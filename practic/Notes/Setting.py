import flet as fl
from Color import Color
from loguru import logger

logger.catch()
def Setting(user, page, dropdown_val=None, color_val="#000000"):
    logger.info("Rendering a page of setting")

    # Очищаем содержимое страницы
    page.controls.clear()

    # AppBar с иконкой возврата
    create_object_setting(user, page)

    #Область для работы с цветами
    setting_color(user, page, dropdown_val, color_val)

    # Обновляем страницу
    page.update()

logger.catch()
def setting_color(user, page, dropdown_val=None, color_val="#000000"):

    dropdown, input_color, save_button = create_object_color_setting(user, page, dropdown_val, color_val)

    # Добавляем элементы на страницу
    page.add(
        fl.Column(
            controls=[
                dropdown,
                input_color,
                save_button
            ]
        )
    )

logger.catch()


def save_new_color(user, page, dropdown, input_color):
    try:
        # Получаем значения из выпадающего списка и поля ввода
        element = dropdown.value
        value = input_color.value

        # Проверка на наличие выбранного элемента и цвета
        if not element:
            logger.warning("No element selected for color change.")
            # Добавляем вывод или предупреждение для пользователя
            page.snack_bar = fl.SnackBar(content=fl.Text("Please select an element to change the color"), open=True)
            page.update()
            return

        if not value:
            logger.warning("No color value provided.")
            page.snack_bar = fl.SnackBar(content=fl.Text("Please enter a valid color value"), open=True)
            page.update()
            return

        # Изменяем цвет элемента
        Color.change_color(user, element, value)

        # Обновляем фон страницы, если выбран элемент "background"
        if element == "background":
            page.bgcolor = value

        logger.info(f"Changing the color of {element} to {value}")

        # Перезагружаем страницу настроек с новыми цветами
        Setting(user, page, element, value)

    except Exception as ex:
        logger.error(f"Ошибка: {ex}")
        page.snack_bar = fl.SnackBar(content=fl.Text(f"Error: {ex}"), open=True)
        page.update()


logger.catch()
def create_object_color_setting(user, page, dropdown_val, color_val):
    # Выпадающий список с элементами для изменения цвета
    dropdown = fl.Dropdown(
        label="Select element",
        options=[fl.dropdown.Option(k) for k in Color.color_user.keys() if not k.startswith("__")],
        value=dropdown_val,
        text_style=fl.TextStyle(color="green"),
        label_style=fl.TextStyle(color="black")
    )

    # Поле ввода для HEX цвета
    input_color = fl.TextField(label="Enter HEX color", value=color_val, text_style=fl.TextStyle(color="black"), label_style=fl.TextStyle(color="black"))

    # Кнопка сохранения
    save_button = fl.IconButton(
        fl.icons.SAVE,
        icon_color=Color.color_user["button"],
        on_click=lambda e: save_new_color(user, page, dropdown, input_color)
    )

    return dropdown, input_color, save_button

logger.catch()
def create_object_setting(user, page):
    from Main_page import show_main_page

    page.add(fl.AppBar(
        center_title=True,
        bgcolor=Color.color_user["appbar_setting"],
        title=fl.Text("Setting", color=Color.color_user["text"]),
        leading=(
            fl.IconButton(
                fl.icons.ARROW_BACK,
                icon_color=Color.color_user["button"],
                on_click=lambda e: show_main_page(user, page)
            )
        )
    ))