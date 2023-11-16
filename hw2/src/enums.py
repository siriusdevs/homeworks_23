"""Contain all the enum classes for hw2."""

from enum import Enum


class Period(Enum):
    """Represent all the necessary periods in days."""

    two_days = 2
    week = 7
    month = 31
    half_of_year = 182
