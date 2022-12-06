import doctest
from typing import Union, Any


class Notebook:
    def __init__(self, type_of_notebook: str, number_of_sheets: int,
                 for_what_subject: str):
        """
        Создание и подготовка к работе объекта "Тетрадь".

        :param type_of_notebook: Вид тетради;
        :param number_of_sheets: Число страниц в тетради;
        :param for_what_subject: Для какого предмета тетрадь.

        Примеры:
        >>> notebook_1 = Notebook("В линию", 80, "Русский язык")
        >>> notebook_2 = Notebook("Без разлиновки", 2, "Для наклеек с котиками")
        """
        if not isinstance(type_of_notebook, str):
            raise TypeError(f"Вид тетради должен быть типом str, "
                            f"а не {type(type_of_notebook)}.")
        self.type_of_notebook = type_of_notebook

        if not isinstance(number_of_sheets, int):
            raise TypeError(f"Количество страниц должно быть типом int, "
                            f"а не {type(number_of_sheets)}.")
        if number_of_sheets <= 0:
            raise ValueError("Количество страниц должено быть "
                             "положительным числом.")
        self.number_of_sheets = number_of_sheets

        if not isinstance(for_what_subject, str):
            raise TypeError(f"Название предмета должно быть типом str, "
                            f"а не {type(for_what_subject)}.")
        self.for_what_subject = for_what_subject

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
            raise ValueError("Количество удаляемых страниц должено быть положительным числом.")
        if number_of_pages_removed > self.number_of_sheets:
            raise ValueError("Количество удаляемых страниц должено быть больше имеющихся страниц.")
        ...

    def add_sheets_to_notebook(self, number_of_pages_added: int) -> None:
        """
        Добавление страниц в тетрадь.

        :param number_of_pages_added: Число добавляемых страниц.

        Примеры:
        >>> notebook_1 = Notebook("Без разлиновки", 4, "Для наклеек с котиками")
        >>> notebook_1.add_sheets_to_notebook(90)
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
    def __init__(self, doll_name: str, doll_sizes: dict[str, Union[int, float]],
                 type_of_clothing: Union[str, None] = None,
                 clothes_size: Union[int, float, None] = None):
        """
        Создание и подготовка к работе объекта "Кукла".

        :param doll_name: Имя куклы;
        :param doll_sizes: Размеры куклы в сантиметрах;
        :param type_of_clothing: Тип одежды, которую наденут на куклу;
        :param clothes_size: Размер одежды в сантиметрах.

        Примеры:
        >>> doll_1 = Doll("Катя", {"Рост": 15.5, "Обхват талии": 3,}, "Куртка", 2.5)
        >>> doll_2 = Doll("Виктор", {"Рост": 22, "Обхват талии": 5,})
        """
        if not isinstance(doll_name, str):
            raise TypeError(f"Имя куклы должно быть типом str, "
                            f"а не {type(doll_name)}.")
        self.doll_name = doll_name

        if not isinstance(doll_sizes, dict):
            raise TypeError(f"Размеры куклы должны быть типом dict, "
                            f"а не {type(doll_sizes)}.")
        for parameter, value in doll_sizes.items():
            if not isinstance(parameter, str):
                raise TypeError(f"Название параметра должено быть типом str, "
                                f"а не {type(parameter)}.")
            if not isinstance(value, (int, float)):
                raise TypeError(f"Параметр должен быть типом str, "
                                f"а не {type(value)}.")
        self.doll_sizes = doll_sizes

        if not isinstance(type_of_clothing, str) and type_of_clothing is not None:
            raise TypeError(f"Тип одежды должен быть типом str или None, "
                            f"а не {type(type_of_clothing)}.")
        self.type_of_clothing = type_of_clothing

        if not isinstance(clothes_size, (int, float)) and type_of_clothing is not None:
            raise TypeError(f"Размер одежды должен быть типом int, float или None, "
                            f"а не {type(clothes_size)}.")
        self.clothes_size = clothes_size

    def dress_up_the_doll(self) -> str:
        """
        Наряжает куклу.

        :return: Как выглядит кукла в примеряемой одежде.

        Примеры:
        >>> doll_1 = Doll("Катя", {"Рост": 15.5, "Обхват талии": 3}, "Куртка", 2.5)
        >>> doll_1.dress_up_the_doll()
        """
        ...

    def presence_of_clothes_on_the_doll(self) -> str:
        """
        Проверяет наличие одежды на кукле.

        :return: Есть ли одежда на кукле или нет.

        Примеры:
        >>> doll_1 = Doll("Полина", {"Рост": 32, "Обхват талии": 6})
        >>> doll_1.presence_of_clothes_on_the_doll()
        """
        ...


class GrandpaForgotToTakeHisPills:
    def __init__(self, tablet_name: str, dose: Union[int, float],
                 when_start_taking_pill: str, interval_between_doses: int):
        """
        Создание и подготовка к работе объекта "Напоминание о таблетке".

        :param tablet_name: Название таблетки;
        :param dose: Доза активного вещества в граммах;
        :param when_start_taking_pill: Дата начала приема таблетки;
        :param interval_between_doses: Интервал между приемами в днях.

        Примеры:
        >>> pill_1 = GrandpaForgotToTakeHisPills("Антидеприссин", 40, "06.12.2022", 7)
        >>> pill_2 = GrandpaForgotToTakeHisPills("Незабывин", 12, "01.12.2022", 3)
        """
        if not isinstance(tablet_name, str):
            raise TypeError(f"Название таблеток должно быть типом str, "
                            f"а не {type(tablet_name)}.")
        self.tablet_name = tablet_name

        if not isinstance(dose, (int, float)):
            raise TypeError(f"Доза должна быть типом int или float, "
                            f"а не {type(dose)}.")
        if dose <= 0:
            raise ValueError("Доза должна быть положительным числом.")
        self.dose = dose

        if not isinstance(when_start_taking_pill, str):
            raise TypeError(f"Дата должна быть типом str, "
                            f"а не {type(when_start_taking_pill)}.")
        self.when_start_taking_pill = when_start_taking_pill

        if not isinstance(interval_between_doses, int):
            raise TypeError(f"Интервал должен быть типом int, "
                            f"а не {type(interval_between_doses)}.")
        if interval_between_doses <= 0:
            raise ValueError("Интервал должен быть положительным числом.")
        self.interval_between_doses = interval_between_doses

    def canitakepilltoday(self, today_s_date: str) -> str:
        """
        Отвечает на вопрос: "Надо ли мне сегодня выпить таблетку?".

        :param today_s_date: Сегодняшний день.

        :return: "Да" или "Нет".

        Примеры:
        >>> pill_1 = GrandpaForgotToTakeHisPills("Антидеприссин", 60, "06.06.2031", 7)
        >>> pill_1.canitakepilltoday("04.07.2031")
        """
        if not isinstance(today_s_date, str):
            raise TypeError(f"Дата должна быть типом str, а не {type(today_s_date)}")
        ...

    def whatispill(self) -> str:
        """
        Ищет иструкцию по применению о данной таблетке.

        :return: Текст с инструкцией по применению.

        Примеры:
        >>> pill_1 = GrandpaForgotToTakeHisPills("Антидеприссин", 60, "06.06.2031", 7)
        >>> pill_1.whatispill()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
