"""Module for getting median value in given sequence."""

from typing import Optional, Sequence


def get_median(sequence: Sequence[float | int], is_sorted: Optional[bool] = False) -> float | int:
    """Calculate median in transmitted sequence.

    Args:
        sequence: Sequence of any int or float item.
        is_sorted: is given sequence sorted? if isn't, he will be (immutable!), default = False.

    Returns:
        median value of items.
    """
    length = len(sequence)
    centre_index = (length - 1) // 2
    new_sequence = list(sequence)

    if length == 0:
        return 0

    if not is_sorted:
        new_sequence.sort()

    if length % 2 == 1:
        return new_sequence[centre_index]

    return (new_sequence[centre_index] + new_sequence[centre_index + 1]) / 2
