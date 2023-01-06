import doctest
from typing import List
from pydantic import BaseModel, StrictInt, validator


BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book(BaseModel):
    """
    Создает экземпляр книги.

    :param id_: Идентификатор книги;
    :param name: Название книги;
    :param pages: Количество страниц в книге.

    Пример:
    >>> book_1 = Book(id_=67, name="Гордость и предубеждение", pages=589)
    """

    id_: StrictInt
    name: str
    pages: StrictInt

    @validator("id_")
    def id_than_zero(cls, var):
        if var <= 0:
            raise ValueError(f"Идентификатор книги должен быть положительным.")
        return var

    @validator("pages")
    def pages_greater_than_zero(cls, var):
        if var <= 0:
            raise ValueError(
                f"Число страниц в книге должно быть положительным.")
        return var


class Library(BaseModel):
    """
    Создает экземпляр книги.

    :param books: Список, состоящий из экземпляров класса Book.

    Пример:
    >>> library_1 = Library(books=[Book(id_=1, name="Гордость и предубеждение", pages=589),\
            Book(id_=2, name="Моцарт и Сальери", pages=35)])
    """
    books: List[Book] = []

    def get_next_book_id(self) -> int:
        """
        Возвращающает идентификатор для добавления новой книги в библиотеку.

        Пример:
        >>> library_1 = Library(books=[Book(id_=78, name="Гордость и предубеждение", pages=589),\
                Book(id_=79, name="Моцарт и Сальери", pages=35)])
        >>> library_1.get_next_book_id()
        80
        """
        if self.books:
            return self.books[-1].id_ + 1
        return 1

    def get_index_by_book_id(self, new_id: int) -> int:
        """
        Возвращающает индекс книги в списке, который хранится в атрибуте экземпляра класса.

        :param new_id: Индекс нужной книги.

        Пример:
        >>> library_1 = Library(books=[Book(id_=1, name="Гордость и предубеждение", pages=589),\
                Book(id_=2, name="Моцарт и Сальери", pages=35)])
        >>> library_1.get_index_by_book_id(2)
        1
        """
        if not isinstance(new_id, int):
            raise TypeError("Id книги должно быть типом int.")
        if new_id < 0:
            raise ValueError("Id книги должно быть положительным числом.")

        for index, book in enumerate(self.books):
            if book.id_ == new_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует.")


if __name__ == '__main__':
    doctest.testmod()

    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки
    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
    print(library_with_books.get_index_by_book_id(5))  # проверяем индекс книги с id = 5
