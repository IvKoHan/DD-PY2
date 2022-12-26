import doctest
from typing import Union, Any


class Notebook:
    def __init__(self, ruler: str, number_of_sheets: int,
                 subject: str):
        """
        Создание и подготовка к работе объекта "Тетрадь".

        :param ruler: Линовка;
        :param number_of_sheets: Число страниц в тетради;
        :param subject: Для какого предмета тетрадь.

        Примеры:
        >>> notebook_1 = Notebook("В линию", 80, "Русский язык")
        >>> notebook_2 = Notebook("Без разлиновки", 2, "Для наклеек с котиками")
        """
        if not isinstance(ruler, str):
            raise TypeError(f"Вид тетради должен быть типом str, "
                            f"а не {type(ruler)}.")
        self.ruler = ruler

        if not isinstance(number_of_sheets, int):
            raise TypeError(f"Количество страниц должно быть типом int, "
                            f"а не {type(number_of_sheets)}.")
        if number_of_sheets <= 0:
            raise ValueError("Количество страниц должно быть "
                             "положительным числом.")
        self.number_of_sheets = number_of_sheets

        if not isinstance(subject, str):
            raise TypeError(f"Название предмета должно быть типом str, "
                            f"а не {type(subject)}.")
        self.subject = subject

    def delete_pages(self, number_of_pages_removed: int) -> None:
        """
        Удаление страниц из тетради.

        :param number_of_pages_removed: Число удаляемых страниц.
        :raise ValueError: Если количество удаляемых страниц превышает
         изначальное число страниц в тетради,
        то возвращается ошибка.

        Примеры:
        >>> notebook_1 = Notebook("Без разлиновки", 34, "Для наклеек с котиками")
        >>> notebook_1.delete_pages(5)
        """
        if not isinstance(number_of_pages_removed, int):
            raise TypeError(f"Количество удаляемых страниц должно быть типом int,"
                            f" а не {type(number_of_pages_removed)}.")
        if number_of_pages_removed <= 0:
            raise ValueError("Количество удаляемых страниц должно быть положительным числом.")
        if number_of_pages_removed > self.number_of_sheets:
            raise ValueError("Количество удаляемых страниц не должно быть больше числа имеющихся страниц.")
        ...

    def add_sheets(self, number_of_pages_added: int) -> None:
        """
        Добавление страниц в тетрадь.

        :param number_of_pages_added: Число добавляемых страниц.

        Примеры:
        >>> notebook_1 = Notebook("Без разлиновки", 4, "Для наклеек с котиками")
        >>> notebook_1.add_sheets(90)
        """
        if not isinstance(number_of_pages_added, int):
            raise TypeError(f"Количество добавляемых страниц должно быть типом int, "
                            f"а не {type(number_of_pages_added)}.")
        if number_of_pages_added <= 0:
            raise ValueError("Количество добавляемых страниц должено быть положительным числом.")
        ...

    def add_entry_to_notebook(self, *entry: Any) -> None:
        """
        Добавление записи в тетрадь.

        :param entry: Записываемая информация в тетрадь.

        Примеры:
        >>> notebook_1 = Notebook("Без разлиновки", 4, "Для наклеек с котиками")
        >>> notebook_1.add_entry_to_notebook({"Имя": "Крекер", "Порода": "Сомали", "Возраст": "2 года"},\
                                             "История одной маленькой кошки...", 6)
        """
        ...


class Doll:
    def __init__(self, doll_name: str, doll_length: Union[int, float],
                 doll_width: Union[int, float], type_of_clothing: Union[str, None] = None,
                 clothes_size: Union[int, float, None] = None):
        """
        Создание и подготовка к работе объекта "Кукла".

        :param doll_name: Имя куклы;
        :param doll_length: Длина куклы в сантиметрах;
        :param doll_width: Ширина куклы в сантиметрах;
        :param type_of_clothing: Тип одежды, которую наденут на куклу;
        :param clothes_size: Размер одежды в сантиметрах.

        Примеры:
        >>> doll_1 = Doll("Катя", 24.5, 5, "Куртка", 2.5)
        >>> doll_2 = Doll("Виктор", 22, 5,)
        """
        if not isinstance(doll_name, str):
            raise TypeError(f"Имя куклы должно быть типом str, "
                            f"а не {type(doll_name)}.")
        self.doll_name = doll_name

        if not isinstance(doll_length, (int, float)):
            raise TypeError(f"Длина куклы должны быть типом int или float, "
                            f"а не {type(doll_length)}.")
        self.doll_length = doll_length

        if not isinstance(doll_width, (int, float)):
            raise TypeError(f"Ширина куклы должны быть типом int или float, "
                            f"а не {type(doll_width)}.")
        self.doll_width = doll_width

        if not isinstance(type_of_clothing, str) and type_of_clothing is not None:
            raise TypeError(f"Тип одежды должен быть типом str или None, "
                            f"а не {type(type_of_clothing)}.")
        self.type_of_clothing = type_of_clothing

        if not isinstance(clothes_size, (int, float)) and type_of_clothing is not None:
            raise TypeError(f"Размер одежды должен быть типом int, float или None, "
                            f"а не {type(clothes_size)}.")
        self.clothes_size = clothes_size

    def dress_up(self) -> str:
        """
        Наряжает куклу.

        :return: Как выглядит кукла в примеряемой одежде.

        Примеры:
        >>> doll_1 = Doll("Катя", 15.5,  3, "Куртка", 2.5)
        >>> doll_1.dress_up()
        """
        ...

    def clothes_presence(self) -> str:
        """
        Проверяет наличие одежды на кукле.

        :return: Есть ли одежда на кукле или нет.

        Примеры:
        >>> doll_1 = Doll("Полина", 32, 6)
        >>> doll_1.clothes_presence()
        """
        ...


class PillsReminder:
    def __init__(self, pill_name: str, dose: Union[int, float],
                 start_date: str, interval: int):
        """
        Создание и подготовка к работе объекта "Напоминание о таблетке".

        :param pill_name: Название таблетки;
        :param dose: Доза активного вещества в граммах;
        :param start_date: Дата начала приема таблетки;
        :param interval: Интервал между приемами в днях.

        Примеры:
        >>> pills_reminder_1 = PillsReminder("Антидеприссин", 40, "06.12.2022", 7)
        >>> pills_reminder_2 = PillsReminder("Незабывин", 12, "01.12.2022", 3)
        """
        if not isinstance(pill_name, str):
            raise TypeError(f"Название таблеток должно быть типом str, "
                            f"а не {type(pill_name)}.")
        self.pill_name = pill_name

        if not isinstance(dose, (int, float)):
            raise TypeError(f"Доза должна быть типом int или float, "
                            f"а не {type(dose)}.")
        if dose <= 0:
            raise ValueError("Доза должна быть положительным числом.")
        self.dose = dose

        if not isinstance(start_date, str):
            raise TypeError(f"Дата должна быть типом str, а не {type(start_date)}.")
        self.start_date = start_date

        if not isinstance(interval, int):
            raise TypeError(f"Интервал должен быть типом int, а не {type(interval)}.")
        if interval <= 0:
            raise ValueError("Интервал должен быть положительным числом.")
        self.interval = interval

    def is_pills_day(self, day: str) -> str:
        """
        Отвечает на вопрос: "Надо ли мне сегодня выпить таблетку?".

        :param day: Сегодняшний день.

        :return: "Да" или "Нет".

        Примеры:
        >>> pills_reminder_1 = PillsReminder("Антидеприссин", 60, "06.06.2031", 7)
        >>> pills_reminder_1.is_pills_day("04.07.2031")
        """
        if not isinstance(day, str):
            raise TypeError(f"Дата должна быть типом str, а не {type(day)}")
        ...

    def pill_instruction(self) -> str:
        """
        Ищет иструкцию по применению о данной таблетке.

        :return: Текст с инструкцией по применению.

        Примеры:
        >>> pills_reminder_1 = PillsReminder("Антидеприссин", 60, "06.06.2031", 7)
        >>> pills_reminder_1.pill_instruction()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
