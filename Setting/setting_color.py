import flet as fl
from loguru import logger
import sys
import string

sys.path.append("..")
from support_modul.Color import Color



def toggle_color_setting(user, page, dropdown_val, color_val, state):
    # Убираем глобальное объявление is_color_setting_visible и используем state
    if state.is_color_setting_visible:
        state.container.content = None  # Убираем содержимое контейнера
    else:
        # Создаем элементы интерфейса настройки цвета
        dropdown, input_color, save_button1, red_slider, green_slider, blue_slider, color_display, Or, rgb_value_text, save_button2 = create_object_color_setting(
            user, page, dropdown_val, color_val)

        # Обновляем содержимое контейнера
        state.container.content = fl.Column(
            controls=[dropdown, fl.Row([input_color, save_button1]),
                      Or, red_slider, green_slider, blue_slider,
                      fl.Row([color_display, rgb_value_text, save_button2])]
        )

    # Переключаем видимость настройки цвета
    state.is_color_setting_visible = not state.is_color_setting_visible

    # Обновляем страницу и контейнер
    page.update()



def save_new_color(user, page, *args):
    try:
        for instance in args:
            if isinstance(instance, fl.Dropdown):
                element = instance.value
            if isinstance(instance, fl.TextField):
                value = instance.value
            if isinstance(instance, fl.Container):
                value = instance.bgcolor

        # Проверка на наличие выбранного элемента и цвета
        if not element:
            logger.warning("No element selected for color change.")
            page.snack_bar = fl.SnackBar(content=fl.Text("Please select an element to change the color"), open=True)
            page.update()
            return

        if not value or len(value) != 7 or  all([sim in '0123456789abcdef' for sim in value]):
            logger.warning("No color value provided.")
            page.snack_bar = fl.SnackBar(content=fl.Text("Please enter a valid color value"), open=True)
            page.update()
            return

        Color.change_color(user, element, value)

        if element == "background":
            page.bgcolor = value

        logger.info(f"Changing the color of {element} to {value}")

        from Setting.Setting import Setting
        Setting(user, page, element, value)

    except Exception as ex:
        logger.error(f"Ошибка: {ex}")
        page.snack_bar = fl.SnackBar(content=fl.Text(f"Error: {ex}"), open=True)
        page.update()


def create_object_color_setting(user, page, dropdown_val, color_val):
    global red_slider, green_slider, blue_slider, color_display, rgb_value_text

    # def dropdown_color_change(e):
    #     if dropdown.text_style.color == 'white':
    #         dropdown.text_style.color = 'black'
    #     else: dropdown.text_style.color = 'white'
    #     dropdown.update()
    #     page.update()

    # Выпадающий список с элементами для изменения цвета
    dropdown = fl.Dropdown(
        label="Select element",
        options=[fl.dropdown.Option(k) for k in Color.color_user.keys() if not k.startswith("__")],
        value=dropdown_val,
        text_style=fl.TextStyle(color="green"),  # Белый цвет для раскрывающегося списка
        label_style=fl.TextStyle(color="black"),
        # on_click=lambda e: dropdown_color_change(e)
    )

    # Поле ввода для HEX цвета
    input_color = fl.TextField(label="Enter HEX color", value=color_val, text_style=fl.TextStyle(color="black"),
                               label_style=fl.TextStyle(color="black"))

    # Кнопка сохранения
    save_button1 = fl.IconButton(
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

    r = red_slider.value
    g = green_slider.value
    b = blue_slider.value


    color_display = fl.Container(
        width=400,
        height=200,
        bgcolor=f"#{value_color_to_hex(r)}{value_color_to_hex(g)}{value_color_to_hex(b)}"
    )
    Or = fl.Text("or", size = 20, color=Color.color_user["text"])
    rgb_value_text = fl.Text(f"RGB(0, 0, 0)", size=20, color=Color.color_user["text"])

    save_button2 = fl.IconButton(
        fl.icons.SAVE,
        icon_color=Color.color_user["button"],
        on_click=lambda e: save_new_color(user, page, dropdown, color_display)
    )

    return dropdown, input_color, save_button1, red_slider, green_slider, blue_slider, color_display, Or, rgb_value_text, save_button2


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