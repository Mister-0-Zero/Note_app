import flet as fl
from flet import AppBar, Text, Container


class Note(Container):
    def __init__(self, title, content, *args, **kwargs):
        super().__init__(
            height=200,
            width=200,
            padding=10,  # Задаем конкретное значение для padding
            border_radius=10,
            border=fl.border.all(1, "black"),
            bgcolor="#407375",
            content=fl.Column([
                Text(title, size=18, italic=True, weight="bold"),
                Text(content, overflow="clip")
            ],
            alignment="start",
            spacing=10  # Используем пиксели для spacing
            ),
            alignment=fl.alignment.center  # Исправлено написание alignment
        )


def main(page: fl.Page):
    page.title = "Notes"
    page.appbar = AppBar(
        title=Text("Заметки", size=24),
        center_title=True,
    )
    page.add(Note("Первая заметка", "Это невероятно, я наконец-то начал писать интерфейсы, а раньше понять не мог как их делают, ема круто!"))
    page.update()

fl.app(target=main)
