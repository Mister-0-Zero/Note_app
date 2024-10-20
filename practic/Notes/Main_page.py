import flet as fl
from AddElInt import Appbar
from Color import Color
from Note import Note
from loguru import logger
import sqlite3 as sq


def show_main_page(user, page):
    logger.info("Rendering the main page")

    # Очищаем элементы страницы перед рендерингом
    page.controls.clear()

    # Устанавливаем цвет фона страницы
    page.bgcolor = Color.color_user["background"]

    # Добавляем AppBar на страницу
    Appbar(user, page)

    # Кнопка удаления всех заметок
    DELETE = fl.FloatingActionButton(
        icon=fl.icons.DELETE,
        bgcolor=Color.color_user["button"],
        on_click=lambda e: delete_all_note(user, page),
    )

    # Кнопка добавления новой заметки
    ADD = fl.FloatingActionButton(
        icon=fl.icons.ADD,
        bgcolor=Color.color_user["button"],
        on_click=lambda e: Note.create_note(user, page),  # Обработка события добавления новой заметки
    )

    # Получаем список заметок из базы данных
    list_notes = []
    with sq.connect("user_notes.db") as con:
        cur = con.cursor()
        list_notes = cur.execute("SELECT title, content FROM notes").fetchall()

    # Рендер всех заметок из списка
    note_containers = []
    for title, content in list_notes:
        note_containers.append(
            fl.Container(
                fl.Text(f"{title}: {content}"),
                col={"xs": 12, "sm": 6, "md": 4, "lg": 3, "xl": 2},
            )
        )

    # Основной контент с заметками
    page.add(
        fl.Column(
            controls=[
                fl.ResponsiveRow(controls=note_containers)
            ],
            expand=True  # Растягиваем основной контент по всей высоте страницы
        )
    )

    # Размещение кнопок в правом нижнем углу с использованием fl.Stack
    page.add(
        fl.Stack(
            controls=[
                fl.Container(
                    DELETE,
                    alignment=fl.alignment.bottom_right,  # Кнопка удаления чуть выше
                    margin=fl.margin.only(right=16, bottom=16),  # Отступ для кнопки удаления
                ),
                fl.Container(
                    ADD,
                    alignment=fl.alignment.bottom_right,  # Кнопка добавления в правом нижнем углу
                    margin=fl.margin.only(right=16, bottom=80),  # Отступ для кнопки добавления
                ),
            ],
            expand=True  # Обеспечиваем, что stack займет всё пространство страницы
        )
    )

    # Обновляем страницу
    page.update()


def delete_all_note(user, page):
    with sq.connect("user_notes.db") as con:
        cur = con.cursor()
        cur.execute("DELETE FROM notes WHERE user_name=?", (user,))
        con.commit()
        logger.info("Notes were deleted from database")

    # Перезагружаем главную страницу после удаления заметок
    show_main_page(user, page)
