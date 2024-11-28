from app.Library import Library


class LibraryConsoleApp:

    def __init__(self):
        self.library = Library()

    # Функция для отображения пунктов меню
    def show_menu(self):
        print("Выберите действие:")
        print("1. Показать все книги")
        print("2. Добавить книгу")
        print("3. Изменить статус книги")
        print("4. Удалить книгу")
        print("5. Поиск")
        print("6. Выход")

    # Основная функция запускающая выбор пользователя
    def run(self):
        actions = {
            "1": self.library.show_books,
            "2": self.add_book,
            "3": self.change_status_book,
            "4": self.delete_book,
            "5": self.found_book,
            "6": self.exit_program
        }

        while True:
            self.show_menu()
            choise = input('Введите номер действия:')

            action = actions.get(choise)
            if action:
                action()
            else:
                print('Такого нет')

    # Функция для добавления книги
    def add_book(self):
        title = input('Введите название книги')
        author = input('Введите автора книги')
        year = int(input("Введите год создания книги"))
        self.library.add_book(title=title, author=author, year=year)

    # Функция для изменения статуса книги
    def change_status_book(self):
        try:
            book_id = int(input("Введите ID книги: "))
            status = int(input("Введите новый статус: (1 - В наличии, 2 - Выдана): "))
        except ValueError:
            print('Некорректный ввод! данные должны быть целым числом')
            return
        if status == 1:
            status = 'В наличии'
        elif status == 2:
            status = 'Выдана'
        else:
            print('Такого статуса НЕТ')
            return
        self.library.change_status(status=status, id=book_id)

    # Функция для удаления книги
    def delete_book(self):
        book_id = int(input("Введите ID книги: "))
        self.library.delete_book(id=book_id)

    # Функция для остановки программы
    def exit_program(self):
        exit(0)

    # Функция для поиска книги по параметрам (Автор, Название, Год)
    def found_book(self):
        key = ''
        try:
            param = int(input('Выберите параметр по которому хотите начать поиск:\n'
                              '1. Названию\n'
                              '2. Автору\n'
                              '3. Году\n'))
            if param == 1:
                key = 'title'
            elif param == 2:
                key = 'author'
            elif param == 3:
                key = 'year'
            else:
                print('Такого параметра НЕТ!')
                return
        except ValueError:
            print('Ввдеите целое число!')
            return
        value = input('Введите данные для поиска')
        self.library.found_book(key=key, value=value)
