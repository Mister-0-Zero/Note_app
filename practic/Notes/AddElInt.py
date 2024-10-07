import flet as fl

def Appbar(page):
    page.add(fl.AppBar(
        center_title=True,
        bgcolor="#ffffff",
        title=fl.Text("Notes", color="#000000"),
        actions=[
            fl.IconButton(
                fl.icons.SETTINGS,
                on_click=action_setting(page),
                icon_color="#000000"
            )
        ]
    ))

def action_setting(page):
    pass