import flet as fl
from setting import action_setting

def Appbar(page):
    page.add(fl.AppBar(
        center_title=True,
        bgcolor="#ffffff",
        title=fl.Text("Notes", color="#000000"),
        actions=[
            fl.IconButton(
                fl.icons.SETTINGS,
                on_click=lambda e: action_setting(page),
                icon_color="#000000"
            )
        ]
    ))
    page.update()

