"""Module with the helper that can increment dictionary's field."""


def increment_field(dictionary: dict[str, int], field_key: str) -> None:
    """Increment dictionary's field.

    Args:
        dictionary (dict[str, int]): given dictionary.
        field_key (str): needed field's key.
    """
    if field_key in dictionary.keys():
        dictionary[field_key] += 1
    else:
        dictionary[field_key] = 1
