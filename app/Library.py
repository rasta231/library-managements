import json
from app.Book import Book
import os


class Library:
    def __init__(self):
        self.file_path = 'library.json'
        self._ensure_file_exists()

    #Функция для открытия и закрытия json файла
    def edit_file(self, mode: str, data=None):
        try:
            if mode == 'r':
                with open(self.file_path, 'r') as file:
                    return json.load(file)
            elif mode == 'w':
                with open(self.file_path, 'w') as file:
                    json.dump(data, file, indent=4, ensure_ascii=False)
            else:
                raise ValueError("Некорректный режим работы или отсутствуют данные для записи")
        except (FileNotFoundError, json.JSONDecodeError):
            print("Библиотека пуста или файл повреждён")
            return []

   #Функция для проверки наличия файла
    def _ensure_file_exists(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as file:
                json.dump([], file)
            print(f"Файл '{self.file_path}' создан")
        else:
            print(f"Файл '{self.file_path}' уже существует")

    #Функция для добавлениея книги
    def add_book(self, title: str, author: str, year: int):
        status = 'В наличии'

        try:
            content = self.edit_file(mode='r')
        except (FileNotFoundError, json.JSONDecodeError):
            content = []

        existing_ids = {book['id'] for book in content}
        new_id = max(existing_ids, default=0) + 1

        new_book = {
            'id': new_id,
            'title': title,
            'author': author,
            'year': year,
            'status': status
        }

        content.append(new_book)

        self.edit_file(mode='w', data=content)
        print(f"Книга '{title}' добавлена в библиотеку с ID {new_id}.")

    # Функция для отображения всех книг
    def show_books(self):
        content = self.edit_file(mode='r')
        if not content:
            print("Библиотека пуста.")
        else:
            for book in content:
                print(book)

    # Функция для поиска книг
    def found_book(self, key: str, value):
        found_books = []
        content = self.edit_file(mode='r')
        for book in content:
            book_value = book.get(key, '')
            if str(book_value).lower() == str(value).lower():
                found_books.append(book)
        if found_books:
            for book in found_books:
                print(book)
        else:
            print("Книга не найдена.")

    # Функция для удаления книги
    def delete_book(self, id: int):
        book_found = False
        updated_content = []
        content = self.edit_file(mode='r')
        for book in content:
            if book.get('id') == id:
                book_found = True
                print(f"Книга '{book['title']}' удалена.")
            else:
                updated_content.append(book)

        if book_found:
            self.edit_file(mode='w', data=updated_content)
        else:
            print('Такой книги не существует.')

    # Функция для изменения статуса книги
    def change_status(self, status: str, id: int):
        book_found = False
        updated_content = []
        content = self.edit_file(mode='r')
        for book in content:
            if book.get('id') == id:
                book['status'] = status
                book_found = True
            updated_content.append(book)

        if book_found:
            self.edit_file(mode='w', data=updated_content)
            print(f"Статус книги с ID {id} изменён на '{status}'.")
        else:
            print('Такой книги нет.')
