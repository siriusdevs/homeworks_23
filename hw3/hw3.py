"""Module that provides types and functions for solving hw3.

Учет авиарейсов и пассажиров

Опишем архитектуру классов для учета авиарейсов и пассажиров.
В этом задании мы будем использовать наследование, инкапсуляцию и композицию.

Класс "Авиарейс":
Поля:
Номер рейса
Аэропорт отправления
Аэропорт прибытия
Методы:
Геттеры и сеттеры для полей

Класс "Пассажир":
Поля:
Имя пассажира
Номер паспорта
Методы:
Геттеры и сеттеры для полей

Класс "Билет":
Поля:
Номер билета
Авиарейс, на который куплен билет (объект класса "Авиарейс")
Пассажир, которому принадлежит билет (объект класса "Пассажир")
Методы:
Геттеры и сеттеры для полей

Класс "Авиакомпания":
Поля:
Название авиакомпании
Список авиарейсов (массив или список объектов класса "Авиарейс")
Список пассажиров (массив или список объектов класса "Пассажир")
Список билетов (массив или список объектов класса "Билет")
Методы:
Геттеры и сеттеры для полей
Добавить авиарейс
Удалить авиарейс
Добавить пассажира
Удалить пассажира
Купить билет
Отменить билет
"""

from typing import Any, Iterable, Type


def check_type(got: Any, want_type: Type) -> None:
    """Assert that got is of type want_type.

    Args:
        got: value which must have want_type
        want_type: type that you want to assert on

    Raises:
        TypeError: when got does not satisfy want_type
    """
    if not isinstance(got, want_type):
        raise TypeError(f'expected {got} to be of type {want_type}')


def check_elements_types(got: Iterable[Any], want_elem_type: Type) -> None:
    """Execute check_type() for each element of the provided Iterable.

    Args:
        got: Iterable, which elements will be checked
        want_elem_type: type that all provided elements must have
    """
    for got_elem in got:
        check_type(got_elem, want_elem_type)
