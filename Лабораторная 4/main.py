import doctest
from typing import Union


class Employee:
    """
    Documentation for the Employee class.
    The class forms a base for storing data about an employee of the company
    and performs the following actions, described below in the documentation.
    """
    def __init__(self, full_name: str, age: int, seniority: Union[int, float],
                 rate: Union[int, float]):
        """
        Initializing an instance of a class.

        These class attributes are protected due to their key importance
        in the company, as they are used for reporting, statements, orders, and so on.
        Only trusted people with special access rights can have access to them.

        :param _full_name: Full name of the employee;
        :param _age: Age of employee (full years);
        :param _seniority: Work experience in years;
        :param _rate: Employee rate.

        Examples:
        >>> employee_1 = Employee("Pupkina Maria Vyacheslavovna", 34, 9, 38980)
        >>> employee_2 = Employee("Kazakov Viktor Pavlovich", 43, 15.8, 172890.23)
        """
        self._full_name = None
        self._age = None
        self._seniority = None
        self._rate = None

        self.full_name = full_name
        self.age = age
        self.seniority = seniority
        self.rate = rate

    @property
    def full_name(self) -> str:
        """
        Return the full name of the Employee.

        :return: Full name of the Employee.

        Examples:
        >>> employee_1 = Employee("Pupkina Maria Vyacheslavovna", 34, 9, 38980)
        >>> employee_1.full_name
        'Pupkina Maria Vyacheslavovna'
        """
        return self._full_name

    @full_name.setter
    def full_name(self, new_full_name: str) -> None:
        """
        Set the full name of the Employee.

        :param new_full_name: New full name of the Employee.

        :raise TypeError: If full name is not of type str, then an error is returned.

        Examples:
        >>> employee_1 = Employee("pupkina maria vyacheslavovna", 34, 9, 38980)
        >>> employee_1.full_name = "Pupkina Maria Vyacheslavovna"
        >>> print(employee_1.full_name)
        ('Pupkina Maria Vyacheslavovna')
        """
        if not isinstance(new_full_name, str):
            raise TypeError("Full name must be of type str")
        self._full_name = new_full_name

    @property
    def age(self) -> Union[int, float]:
        """
        Return the age of the Employee.

        :return: Age of the Employee.

        Examples:
        >>> employee_1 = Employee("Pupkina Maria Vyacheslavovna", 34, 9, 38980)
        >>> employee_1.age
        34
        """
        return self._age

    @age.setter
    def age(self, new_age: Union[int, float]) -> None:
        """
        Set the age of the Employee.

        :param new_age: New age of the Employee.

        :raise TypeError: If age is not of type int, then an error is returned.
        :raise ValueError: If age is not a positive number within the limit of
        120 years, then an error is returned.

        Examples:
        >>> employee_1 = Employee("Pupkina Maria Vyacheslavovna", 34, 9, 38980)
        >>> employee_1.age = 56
        >>> print(employee_1.age)
        56
        """
        if not isinstance(new_age, int):
            raise TypeError("Age must be of type int")
        if not 0 < new_age <= 120:
            raise ValueError("Age must be a positive number and be within "
                             "the limit of 120 years")
        self._age = new_age

    @property
    def seniority(self) -> Union[int, float]:
        """
        Return the seniority of the Employee.

        :return: Seniority of the Employee.

        Examples:
        >>> employee_1 = Employee("Pupkina Maria Vyacheslavovna", 34, 9, 38980)
        >>> employee_1.seniority
        9
        """
        return self._seniority

    @seniority.setter
    def seniority(self, new_seniority: Union[int, float]) -> None:
        """
        Set the seniority of the Employee.

        :param new_seniority: New seniority of the Employee.

        :raise TypeError: If seniority is not of type int or float, then an error is returned.
        :raise ValueError: If seniority is not a positive number within
        the limit of 100 years and is not under age, then an error is returned.

        Examples:
        >>> employee_1 = Employee("Pupkina Maria Vyacheslavovna", 34, 9, 38980)
        >>> employee_1.seniority = 11
        >>> print(employee_1.seniority)
        11
        """
        if not isinstance(new_seniority, (int, float)):
            raise TypeError("Seniority must be of type int or float")
        if not (0 < new_seniority <= 100 and new_seniority < self._age):
            raise ValueError("Seniority must be a positive number, be within "
                             "the limit of 100 years and be under age")
        self._seniority = new_seniority

    @property
    def rate(self) -> Union[int, float]:
        """
        Return the rate of the Employee.

        :return: Rate of the Employee.

        Examples:
        >>> employee_1 = Employee("Pupkina Maria Vyacheslavovna", 34, 9, 38980)
        >>> employee_1.rate
        38980
        """
        return self._rate

    @rate.setter
    def rate(self, new_rate: Union[int, float]) -> None:
        """
        Set the rate of the Employee.

        :param new_rate: New rate of the Employee.

        :raise TypeError: If rate is not of type int or float, then an error is returned.
        :raise ValueError: If rate is not a positive number, then an error is returned.

        Examples:
        >>> employee_1 = Employee("Pupkina Maria Vyacheslavovna", 34, 9, 38980)
        >>> employee_1.rate = 11876
        >>> print(employee_1.rate)
        11876
        """
        if not isinstance(new_rate, (int, float)):
            raise TypeError("Rate must be of type int or float")
        if not 0 < new_rate:
            raise ValueError("Rate must be a positive number")
        self._rate = new_rate

    def __str__(self) -> str:
        """
        A string representation of the Employee.

        :return: A string representation of the Employee in the form:
                Employee Full Name, Age years old, seniority Seniority years.
                Salary is Salary rubles, deductible tax - Tax rubles.

        Examples:
        >>> employee_1 = Employee("Pupkina Maria Vyacheslavovna", 34, 9, 38980)
        >>> print(employee_1.__str__())
        Employee Pupkina Maria Vyacheslavovna, 34 years old, seniority 9 years.
        Salary is 33912.68 rubles, deductible tax - 5067.41 rubles.
        """
        return f"{self.__class__.__name__} {self._full_name}, " \
               f"{self._age} years old, seniority {self._seniority} years.\n" \
               f"Salary is {self.salary()} rubles, deductible tax - {self.tax()} rubles."

    def __repr__(self) -> str:
        """
        Return a string representation of the Employee object.

        :return: A string representation of the Technologist object in the form:
                Employee(surname='Full Name', age=Age, seniority=Seniority,
                rate=Rate, salary=Salary, tax=Tax)

        Examples:
        >>> employee_1 = Employee("Pupkina Maria Vyacheslavovna", 34, 9, 38980)
        >>> print(employee_1.__repr__())
        Employee(surname='Pupkina Maria Vyacheslavovna', age=34, seniority=9,
        rate=38980, salary=33912.68, tax=5067.41)
        """
        return f"{self.__class__.__name__}(surname={self._full_name!r}, " \
               f"age={self._age!r}, seniority={self._seniority!r},\n" \
               f"rate={self._rate!r}, salary={self.salary()}, tax={self.tax()})"

    def tax(self) -> float:
        """
        Based on the data entered, the tax paid to the state is calculated.

        :return: Tax amount.

        Examples:
        >>> employee_1 = Employee("Pupkina Maria Vyacheslavovna", 34, 9, 38980)
        >>> print(employee_1.tax())
        5067.41
        """
        return round((self._rate + self._seniority / 100) * 0.13, 2)

    def salary(self) -> float:
        """
        Calculates the total amount of wages that are given to the employee.

        :return: Total salary.

        Examples:
        >>> employee_1 = Employee("Pupkina Maria Vyacheslavovna", 34, 9, 38980)
        >>> print(employee_1.salary())
        33912.68
        """
        return round(self._rate + self._seniority / 100 - self.tax(), 2)


class Cleaner(Employee):
    """
    Documentation for the Cleaner class.
    Cleaner is a derived class from the Employee class.
    """
    def __init__(self, full_name: str, age: int, seniority: Union[int, float],
                 rate: Union[int, float]):
        """
        Initializing an instance of a class.

        These class attributes are protected due to their key importance
        in the company, as they are used for reporting, statements, orders, and so on.
        Only trusted people with special access rights can have access to them.

        :param _full_name: Full name of the cleaner;
        :param _age: Age of cleaner (full years);
        :param _seniority: Work experience in years;
        :param _rate: Cleaner rate.

        Example:
        >>> cleaner_2 = Cleaner("Zlobina Lola Afanasievna", 67, 6, 28907.8)
        """
        super().__init__(full_name, age, seniority, rate)

    @staticmethod
    def clean(space: Union[int, float]) -> str:
        """
        Sends a command to the cleaner to clean the specified area.

        :param space: Cleaning area in square meters.

        :return: This place has been cleaned.

        :raise TypeError: If space is not of type int or float, then an error is returned.
        :raise ValueError: If space is not a positive number, then an error is returned.

        Example:
        >>> cleaner_2 = Cleaner("Zlobina Lola Afanasievna", 67, 6, 28907.8)
        >>> print(cleaner_2.clean(30.5))
        This place has been cleaned.
        """
        if not isinstance(space, (int, float)):
            raise TypeError("Space must be of type int or float")
        if not 0 < space:
            raise ValueError("Space must be a positive number")
        ...
        return "This place has been cleaned."


class Technologist(Employee):
    """
    Documentation for the Technologist class.

    A derived class of Employee representing Technologists.
    Technologists are employees who are responsible for developing and
    designing technological places. They have the same attributes as Employees,
    with the addition of a bonus attribute, and the ability to perform development
    tasks represented by the 'develop' method.
    """
    def __init__(self, full_name: str, age: int, seniority: Union[int, float],
                 rate: Union[int, float], bonus: Union[int, float]):
        """
        Initializing an instance of a class.

        These class attributes are protected due to their key importance
        in the company, as they are used for reporting, statements, orders, and so on.
        Only trusted people with special access rights can have access to them.

        :param _full_name: Full name of the technologist;
        :param _age: Age of technologist (full years);
        :param _seniority: Work experience in years;
        :param _rate: Technologist rate.
        :param _bonus: Technologist bonus.

        Examples:
        >>> technologist_1 = Technologist("Kazakov Viktor Pavlovich", 43, 15.8, 172890.23, 20000)
        """
        super().__init__(full_name, age, seniority, rate)
        self._bonus = None
        self.bonus = bonus

    @property
    def bonus(self) -> Union[int, float]:
        """
        Return the bonus of the Technologist.

        :return: bonus of the Technologist.

        Examples:
        >>> technologist_1 = Technologist("Kazakov Viktor Pavlovich", 43, 15.8, 172890.23, 20000)
        >>> technologist_1.bonus
        20000
        """
        return self._bonus

    @bonus.setter
    def bonus(self, new_bonus: Union[int, float]) -> None:
        """
        Set the bonus of the Technologist.

        :param new_bonus: New seniority of the Technologist.

        :raise TypeError: If bonus is not of type int or float, then an error is returned.
        :raise ValueError: If bonus is not a positive number, then an error is returned.

        Examples:
        >>> technologist_1 = Technologist("Kazakov Viktor Pavlovich", 43, 15.8, 172890.23, 20000)
        >>> technologist_1.bonus = 14500
        >>> print(technologist_1.bonus)
        14500
        """
        if not isinstance(new_bonus, (int, float)):
            raise TypeError("Rate must be of type int or float")
        if not 0 < new_bonus:
            raise ValueError("Rate must be a positive number")
        self._bonus = new_bonus

    def __str__(self) -> str:
        """
         A string representation of the Technologist.

         :return: A string representation of the Technologist in the form:
                 Technologist Full Name, Age years old, seniority Seniority years.
                 Salary is Salary rubles, deductible tax - Tax rubles, bonus is Bonus rubles.

         Examples:
         >>> technologist_1 = Technologist("Kazakov Viktor Pavlovich", 43, 15.8, 172890.23, 20000)
         >>> print(technologist_1.__str__())
         Technologist Kazakov Viktor Pavlovich, 43 years old, seniority 15.8 years.
         Salary is 167814.64 rubles, deductible tax - 25075.75 rubles, bonus is 20000 rubles.
         """
        return f"{self.__class__.__name__} {self._full_name}, " \
               f"{self._age} years old, seniority {self._seniority} years.\n" \
               f"Salary is {self.salary()} rubles, deductible tax - {self.tax()} rubles, " \
               f"bonus is {self._bonus} rubles."

    def __repr__(self) -> str:
        """
        Return a string representation of the Technologist object.

        :return: A string representation of the Technologist object in the form:
                Technologist(surname='Full Name', age=Age, seniority=Seniority,
                rate=Rate, salary=Salary, tax=Tax, bonus=Bonus)

        Examples:
        >>> technologist_1 = Technologist("Kazakov Viktor Pavlovich", 43, 15.8, 172890.23, 20000)
        >>> print(technologist_1.__repr__())
        Technologist(surname='Kazakov Viktor Pavlovich', age=43, seniority=15.8,
        rate=172890.23, salary=167814.64, tax=25075.75, bonus=20000)
        """
        return f"{self.__class__.__name__}(surname={self._full_name!r}, " \
               f"age={self._age!r}, seniority={self._seniority!r},\n" \
               f"rate={self._rate!r}, salary={self.salary()}, tax={self.tax()}, " \
               f"bonus={self._bonus!r})"

    def tax(self) -> float:
        return round((self._rate + self._seniority / 100 + self._bonus) * 0.13, 2)

    def salary(self) -> float:
        return round(self._rate + self._seniority / 100 + self._bonus - self.tax(), 2)

    @staticmethod
    def develop(length: Union[int, float], width: Union[int, float],
                height: Union[int, float]) -> str:
        """
        Based on the received data, a written plan of one premises
        of the enterprise is created with a reference to the drawing.

        :param length: Room length in meters;
        :param width: Room width in meters;
        :param height: Room height in meters

        :raise TypeError: If the input width, or height, or length of
        the room is not an int or float, then an error is returned.
        :raise ValueError: If the input width, or height, or length of
        the room is not a positive, then an error is returned.

        :return: Written plan of one premises of the enterprise.
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Length must be of type int or float")
        if not 0 < length:
            raise ValueError("Length must be a positive number")

        if not isinstance(width, (int, float)):
            raise TypeError("Width must be of type int or float")
        if not 0 < width:
            raise ValueError("Width must be a positive number")

        if not isinstance(height, (int, float)):
            raise TypeError("Height must be of type int or float")
        if not 0 < height:
            raise ValueError("Height must be a positive number")
        ...


if __name__ == "__main__":
    doctest.testmod()
