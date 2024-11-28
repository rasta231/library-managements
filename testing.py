import unittest
import json
import os
from app.Book import Book
from app.Library import Library


class TestLibrary(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Инициализация объекта библиотеки перед всеми тестами."""
        cls.library = Library()

    def setUp(self):
        """Очистка библиотеки перед каждым тестом."""
        self.library.edit_file(mode='w', data=[])

    def test_add_book(self):
        """Тест добавления книги."""
        self.library.add_book("Война и мир", "Лев Толстой", 1869)
        books = self.library.edit_file(mode='r')
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]['title'], "Война и мир")
        self.assertEqual(books[0]['author'], "Лев Толстой")
        self.assertEqual(books[0]['year'], 1869)

    def test_delete_book(self):
        """Тест удаления книги."""
        self.library.add_book("Преступление и наказание", "Фёдор Достоевский", 1866)
        book_id = self.library.edit_file(mode='r')[0]['id']
        self.library.delete_book(book_id)
        # Проверяем, что книга удалена
        books = self.library.edit_file(mode='r')
        self.assertEqual(len(books), 0)

    def test_change_status(self):
        """Тест изменения статуса книги."""
        self.library.add_book("Мастер и Маргарита", "Михаил Булгаков", 1967)
        book_id = self.library.edit_file(mode='r')[0]['id']
        self.library.change_status("Выдана", book_id)
        books = self.library.edit_file(mode='r')
        self.assertEqual(books[0]['status'], "Выдана")

    def test_invalid_book_id(self):
        """Тест некорректного ID книги при добавлении."""
        with self.assertRaises(ValueError):
            Book(book_id=-1, title="Некорректная книга", author="Неизвестный", year=2020)

    def test_invalid_year(self):
        """Тест некорректного года при добавлении книги."""
        with self.assertRaises(ValueError):
            Book(book_id=1, title="Некорректная книга", author="Неизвестный", year=-200)

    def test_invalid_string(self):
        """Тест некорректного значения для названия книги."""
        with self.assertRaises(ValueError):
            Book(book_id=1, title="", author="Неизвестный", year=2020)

    def test_invalid_status(self):
        """Тест некорректного статуса при добавлении книги."""
        with self.assertRaises(ValueError):
            Book(book_id=1, title="Неверный статус", author="Неизвестный", year=2020, status="Невозможно")


if __name__ == "__main__":
    unittest.main()
