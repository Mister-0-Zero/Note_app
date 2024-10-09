import flet as fl
from color import Color

class Note(fl.Container):
    list_note = []
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

    @classmethod
    def create_note(cls, page):
        try:
            name_previous_note = cls.list_note[0][-1]
        except:
            name_previous_note = None

        if name_previous_note:
            name_new_note = "Note_" + str(int(name_previous_note[5:]) + 1)
        else:
            name_new_note = "Note_1"
        Note = page.add(cls(
            title="-",
            content="-"
        ))
        cls.list_note.append([name_new_note, Note])