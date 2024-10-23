import flet as fl
from Color import Color
from loguru import logger

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


def toggle_color_setting(user, page, dropdown_val, color_val, container):
    global is_color_setting_visible
    if is_color_setting_visible:
        # Если элементы отображены, скрываем их, очищая контейнер
        container.content = None
    else:
        # Если элементы скрыты, отображаем их
        dropdown, input_color, save_button, red_slider, green_slider, blue_slider, color_display, Or, rgb_value_text = create_object_color_setting(user, page, dropdown_val, color_val)
        container.content = fl.Column(controls=[dropdown, input_color, Or, red_slider, green_slider, blue_slider, fl.Row([color_display, rgb_value_text]), save_button])

    # Переключаем состояние
    is_color_setting_visible = not is_color_setting_visible

    # Обновляем контейнер и страницу
    container.update()
    page.update()


def save_new_color(user, page, dropdown, input_color):
    try:
        # Получаем значения из выпадающего списка и поля ввода
        element = dropdown.value
        value = input_color.value

        # Проверка на наличие выбранного элемента и цвета
        if not element:
            logger.warning("No element selected for color change.")
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


def create_object_color_setting(user, page, dropdown_val, color_val):
    global red_slider, green_slider, blue_slider, color_display, rgb_value_text
    # Выпадающий список с элементами для изменения цвета
    dropdown = fl.Dropdown(
        label="Select element",
        options=[fl.dropdown.Option(k) for k in Color.color_user.keys() if not k.startswith("__")],
        value=dropdown_val,
        text_style=fl.TextStyle(color="green"),
        label_style=fl.TextStyle(color="black")
    )

    # Поле ввода для HEX цвета
    input_color = fl.TextField(label="Enter HEX color", value=color_val, text_style=fl.TextStyle(color="black"),
                               label_style=fl.TextStyle(color="black"))

    # Кнопка сохранения
    save_button = fl.IconButton(
        fl.icons.SAVE,
        icon_color=Color.color_user["button"],
        on_click=lambda e: save_new_color(user, page, dropdown, input_color)
    )

    # Шкала для красного цвета
    red_slider = fl.Slider(min=0, max=255, divisions=255, value=0, label="Red", on_change=lambda e: update_color(e, page))

    # Шкала для зеленого цвета
    green_slider = fl.Slider(min=0, max=255, divisions=255, value=0, label="Green", on_change=lambda e: update_color(e, page))

    # Шкала для синего цвета
    blue_slider = fl.Slider(min=0, max=255, divisions=255, value=0, label="Blue", on_change=lambda e: update_color(e, page))

    color_display = fl.Container(
        width=400,
        height=200,
        bgcolor="#ffffff"
    )
    Or = fl.Text("or", size = 20, color=Color.color_user["text"])
    rgb_value_text = fl.Text(f"RGB(0, 0, 0)", size=20, color=Color.color_user["text"])

    return dropdown, input_color, save_button, red_slider, green_slider, blue_slider, color_display, Or, rgb_value_text

def update_color(e, page):
    # Получаем значения слайдеров
    r = red_slider.value
    g = green_slider.value
    b = blue_slider.value

    # Формируем цвет в формате RGB
    selected_color = f"#{value_color_to_hex(r)}{value_color_to_hex(g)}{value_color_to_hex(b)}"

    # Обновляем цвет дисплея
    color_display.bgcolor = selected_color

    # Обновляем текст с текущими значениями RGB
    rgb_value_text.value = f"RGB({int(r)}, {int(g)}, {int(b)})"

    # Обновляем страницу
    page.update()


def value_color_to_hex(value):
    value = int(value)
    value = hex(value)[2:]
    value = str(value)
    if len(value) < 2:
        return "0" + value
    return value

def create_object_setting(user, page, dropdown_val, color_val):
    from Main_page import show_main_page

    # Создаем AppBar
    page.appbar = fl.AppBar(
        center_title=True,
        bgcolor=Color.color_user["appbar_setting"],
        title=fl.Text("Setting", color=Color.color_user["text"]),
        leading=fl.IconButton(
            fl.icons.ARROW_BACK,
            icon_color=Color.color_user["button"],
            on_click=lambda e: show_main_page(user, page)
        )
    )

    # Контейнер для динамического контента
    container = fl.Container()

    # Текст с событием нажатия, который отображает настройки цвета
    color_set_text = fl.GestureDetector(
        content=fl.Text("-Color setting:", color=Color.color_user["text"], size=20),
        on_tap=lambda e: toggle_color_setting(user, page, dropdown_val, color_val, container)
    )

    # Добавляем элементы на страницу
    page.add(fl.Column([color_set_text, container]))

    # Обновляем страницу
    page.update()
