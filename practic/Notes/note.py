import flet as fl
from color import Color

class Note(fl.Container):
    def __init__(self, title, content, bgcolor="#407375", *args, **kwargs):
        super().__init__(
            height=200,
            width=200,
            padding=10,
            border_radius=10,
            border=fl.border.all(1, "black"),
            bgcolor=bgcolor,
            content=fl.Column([
                fl.Text(title, size=18, italic=True, weight="bold"),
                fl.Text(content, overflow="clip")
            ],
                alignment="start",
                spacing=10
            ),
            alignment=fl.alignment.center
        )