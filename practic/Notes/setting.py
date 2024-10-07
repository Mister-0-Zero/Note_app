import flet as fl
from color import Color

def Setting(page, flag = 0):
    from main_page import show_main_page
    # Очищаем содержимое страницы
    if flag == 0: page.controls.clear()

    # AppBar с иконкой возврата
    page.add(fl.AppBar(
        center_title=True,
        bgcolor=Color.appbar_setting,
        title=fl.Text("Setting", color=Color.text),
        leading=(
            fl.IconButton(
                fl.icons.ARROW_BACK,
                icon_color=Color.button,
                on_click=lambda e: show_main_page(page)
            )
        )
    ))

    if flag == 0: setting_color(page)

    # Обновляем страницу
    if flag == 0: page.update()

def setting_color(page):
    # Выпадающий список с элементами для изменения цвета
    dropdown = fl.Dropdown(
        label="Select element",
        options=[fl.dropdown.Option(k) for k in Color.__dict__.keys() if not k.startswith("__")]
    )

    # Поле ввода для HEX цвета
    input_color = fl.TextField(label="Enter HEX color", value="#000000")

    # Кнопка сохранения
    save_button = fl.IconButton(
        fl.icons.SAVE,
        icon_color=Color.button,
        on_click=lambda e: save_new_color()
    )

    # Функция для сохранения нового цвета
    def save_new_color():
        try:
            # Изменение атрибута класса Color
            setattr(Color, dropdown.value, input_color.value)
            print(f"{dropdown.value} изменен на {input_color.value}")

            # Перезагружаем страницу настроек с новыми цветами
            Setting(page, flag = 1)
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