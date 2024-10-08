import flet as fl
from color import Color

def Setting(user, page, dropdown_val=None, color_val="#000000"):
    from main_page import show_main_page
    # Очищаем содержимое страницы
    page.controls.clear()

    # AppBar с иконкой возврата
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

    setting_color(user, page, dropdown_val, color_val)

    # Обновляем страницу
    page.update()

def setting_color(user, page, dropdown_val=None, color_val="#000000"):
    # Выпадающий список с элементами для изменения цвета
    dropdown = fl.Dropdown(
        label="Select element",
        options=[fl.dropdown.Option(k) for k in Color.color_user.keys() if not k.startswith("__")],
        value=dropdown_val
    )

    # Поле ввода для HEX цвета
    input_color = fl.TextField(label="Enter HEX color", value=color_val)

    # Кнопка сохранения
    save_button = fl.IconButton(
        fl.icons.SAVE,
        icon_color=Color.color_user["button"],
        on_click=lambda e: save_new_color(user, page)
    )

    # Функция для сохранения нового цвета
    def save_new_color(user, page):
        try:
            element = dropdown.value
            color = input_color.value
            # Изменение атрибута класса Color
            setattr(Color, element, color)
            print(f"{dropdown.value} изменен на {input_color.value}")
            Color.change_color(user, element, color)
            if element == "background": page.bgcolor = color

            # Перезагружаем страницу настроек с новыми цветами
            Setting(user, page, element, color)

        except Exception as ex:
            print(f"Ошибка: {ex}")



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

