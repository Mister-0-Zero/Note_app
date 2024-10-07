from note import Note
import AddElInt
import flet as fl

def main(page: fl.Page):
    # Переменная для хранения выбранного цвета фона
    background_color = "#407375"

    # Список для хранения всех заметок
    notes = []

    # Главная страница с заметками
    def show_notes_page():
        page.controls.clear()

        #Добавляем AppBar на страничку
        AddElInt.Appbar(page)



    show_notes_page()

if __name__ == "__main__":
    fl.app(target=main)
