import flet as fl
from flet import AppBar, Text, Container, Row, Stack, Column


class Note(Container):
    def __init__(self, title, content, *args, **kwargs):
        super().__init__(
            height=200,
            width=200,
            padding=10,
            border_radius=10,
            border=fl.border.all(1, "black"),
            bgcolor="#407375",
            content=fl.Column([
                Text(title, size=18, italic=True, weight="bold"),
                Text(content, overflow="clip")
            ],
            alignment="start",
            spacing=10
            ),
            alignment=fl.alignment.center
        )


def main(page: fl.Page):
    # Список для хранения всех заметок
    notes = []


    page.title = "Notes"
    page.appbar = AppBar(
        title=Text("Заметки", size=24),
        center_title=True,
    )

    # Контейнер для заметок с прокруткой
    notes_container = Row(wrap=True, spacing=10)

    # Обертываем контейнер заметок в Column для добавления прокрутки
    scrollable_container = Column(
        controls=[notes_container],
        expand=True,
        scroll="auto"  # Включаем прокрутку, когда содержимое превышает высоту экрана
    )

    # Функция для добавления новой заметки
    def add_note(e):
        new_note = Note("Новая заметка", "Текст заметки")
        notes.append(new_note)
        notes_container.controls.append(new_note)
        page.update()

    def open_set():
        pass
    # Кнопка добавления заметки
    add_button = fl.FloatingActionButton(
        icon=fl.icons.ADD,
        on_click=add_note
    )
    setting_buttom = fl.FloatingActionButton(
        icon = fl.icons.SETTINGS,
        on_click=open_set
    )

    # Создаем главный контейнер Stack, который будет содержать заметки и кнопку
    page.add(
        Stack([
            # Контейнер с заметками
            Container(
                content=scrollable_container,
                expand=True  # Растягиваем на весь экран
            ),
            # Фиксируем кнопку в правом нижнем углу
            Container(
                content=add_button,
                alignment=fl.alignment.bottom_right,  # Выравниваем кнопку в нижнем правом углу
                margin=fl.margin.all(16),
            ),
        ])
    )

    page.update()

fl.app(target=main)
