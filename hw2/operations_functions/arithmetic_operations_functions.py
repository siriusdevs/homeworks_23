"""Module with arithmetic operations functions."""


def get_average(numbers: list[int]) -> int | float:
    """Calculate the average of the numbers.

    Args:
        numbers (list[int]): numbers.

    Returns:
        int | float: the average of the numbers.
    """
    return round(sum(numbers) / len(numbers), 2)


def get_median(numbers: list[int]) -> int | float:
    """Calculate the median of the numbers.

    Args:
        numbers (list[int]): numbers.

    Returns:
        int | float: the median of the numbers.
    """
    numbers = sorted(numbers)
    middle_index = len(numbers) // 2
    if len(numbers) % 2 == 1:
        median_number = numbers[middle_index]
    else:
        two_middle_numbers = [numbers[middle_index - 1]] + [numbers[middle_index]]
        median_number = round(sum(two_middle_numbers) / 2, 2)
    return median_number
