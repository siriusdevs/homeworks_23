"""Module for ages operations."""


def get_median_age(ages: list[int]) -> int:
    """Get median age from list of ages.

    Args:
        ages (list[int]): list of ages

    Returns:
        int: The median age
    """
    sort_ages = sorted(ages)
    len_ages = len(sort_ages)
    half_len_ages = len_ages // 2
    middle_number = sort_ages[half_len_ages]

    if len_ages % 2 == 0:
        return (middle_number + sort_ages[half_len_ages - 1]) // 2

    return middle_number


def get_average_age(ages):
    """Get average age fron ages list.

    Args:
        ages (list[int]): the ages list

    Returns:
        age: the average age.
    """
    len_ages = len(ages)
    if len_ages == 0:
        return 0
    return int(round(sum(ages) / len_ages, 0))
