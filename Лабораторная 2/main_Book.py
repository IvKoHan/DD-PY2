import doctest
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


class Book (BaseModel):
    """
    Создает экземпляр книги.

    :param id_: Идентификатор книги;
    :param name: Название книги;
    :param pages: Количество страниц в книге.

    Пример:
    >>> book_1 = Book(id_=3, name="Отцы и дети", pages=757)
    """
    id_: StrictInt
    name: str
    pages: StrictInt

    @validator("id_")
    def id_than_zero(cls, var):
        if var <= 0:
            raise ValueError(f"Идентификатор книги должен быть положительным")
        return var

    @validator("pages")
    def pages_greater_than_zero(cls, var):
        if var <= 0:
            raise ValueError(f"Число страниц в книге должно быть положительным")
        return var

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})'

    def __str__(self) -> str:
        return f'Книга "{self.name}"'


if __name__ == '__main__':
    doctest.testmod()

    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
