"""hw2 module for all classes-enums."""

from enum import Enum


class Period(Enum):
    """Class-enum representing all the necessary periods."""

    two_days = 2
    week = 7
    month = 31
    half_of_year = 182
