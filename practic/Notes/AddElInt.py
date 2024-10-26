import flet as fl
from Setting.Setting import Setting
from Color import Color

def Appbar(user, page):
    page.add(fl.AppBar(
        center_title=True,
        bgcolor=Color.color_user["appbar_notes"],
        title=fl.Text("Notes", color=Color.color_user["text"]),
        actions=[
            fl.IconButton(
                fl.icons.SETTINGS,
                on_click=lambda e: Setting(user, page),
                icon_color=Color.color_user["button"]
            )
        ]
    ))
    page.update()

