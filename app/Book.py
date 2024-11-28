class Book:
    def __init__(self, book_id: int, title: str, author: str, year: int, status: str = "В наличии"):
        self.id = self._validate_id(book_id)
        self.title = self._validate_string_type_element(title)
        self.author = self._validate_string_type_element(author)
        self.year = self._validate_year(year)
        self.status = self._validate_status(status)

    @staticmethod
    # Функция для валидации id
    def _validate_id(book_id: int) -> int:
        if not isinstance(book_id, int) or book_id <= 0:
            raise ValueError("ID книги должен быть положительным целым числом.")
        return book_id

    @staticmethod
    # Функция для валидации year
    def _validate_year(year: int) -> int:
        if not isinstance(year, int) or year < 0:
            raise ValueError("Год должен быть целым числом больше 0.")
        return year

    @staticmethod
    # Функция для валидации string переменных
    def _validate_string_type_element(value: str) -> str:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Поле должно быть строкой и не может быть пустым.")
        return value.strip()

    @staticmethod
    # Функция для валидации status книги
    def _validate_status(status: str) -> str:
        allowed_statuses = {"В наличии", "Выдана"}
        if status not in allowed_statuses:
            raise ValueError(f"Статус должен быть одним из: {allowed_statuses}.")
        return status

    @property
    #Функция которая возвращет созданыйэ элемент книги
    def element(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }
