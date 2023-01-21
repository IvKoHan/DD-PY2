class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = None
        self.pages = pages

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Страницы {self._pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}," \
               f"author={self._author!r}, pages={self._pages!r})"

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = None
        self.duration = duration

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Продолжительность {self._duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}," \
               f"author={self._author!r}, duration={self._duration!r})"

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = new_duration


if __name__ == '__main__':
    book1 = Book("Прао", "апы")
    print(book1)
    print(dir(book1))
    print(repr(book1))
    print()
    book2 = PaperBook("dfgfrg", "kjkjb", 679)
    print(book2)
    print(dir(book2))
    print(repr(book2))
    print()
    book3 = AudioBook("rfjkli", "mnbvcdgh", -56.7)
    print(book3)
    print(dir(book3))
    print(repr(book3))
