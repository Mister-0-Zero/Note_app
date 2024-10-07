import flet as fl
from setting import Setting
from color import Color

def Appbar(page):
    page.add(fl.AppBar(
        center_title=True,
        bgcolor=Color.appbar_notes,
        title=fl.Text("Notes", color=Color.text),
        actions=[
            fl.IconButton(
                fl.icons.SETTINGS,
                on_click=lambda e: Setting(page),
                icon_color=Color.button
            )
        ]
    ))
    page.update()

