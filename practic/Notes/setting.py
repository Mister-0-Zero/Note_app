import flet as fl


def action_setting(page):
    from main_page import show_main_page

    page.controls.clear()

    page.add(fl.AppBar(
        center_title = True,
        bgcolor = "#ffffff",
        title = fl.Text("Setting", color="#000000"),
        leading=(
                fl.IconButton(
                    fl.icons.ARROW_BACK,
                    icon_color="#000000",
                    on_click=lambda e: show_main_page(page)
                )
            )
    ))

    page.update()