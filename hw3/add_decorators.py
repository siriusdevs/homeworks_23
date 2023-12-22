"""Module with decorators, that add properties and methods."""


from typing import Any, Callable, Type

from check_decorators import check_list_types, check_type

UNDERSCORE = '_'


def add_simple_property(
    property_name: str,
    property_type: Type[Any],
    is_list: bool = False,
) -> Callable:
    """Add getter and setter for property to class.

    Args:
        property_name: name of property you want to add getter and setter
        property_type: type of value that must be in property
        is_list: True if property is list else False

    Returns:
        decorator function
    """
    def wrapper(class_: type) -> type:
        if is_list:
            def _get_property(self) -> list[property_type]:
                return getattr(self, f'{UNDERSCORE}{property_name}')

            def _set_property(self, new_value: list[property_type]) -> None:
                check_list_types(f'{class_.__name__} {property_name}', new_value, property_type)
                setattr(self, f'{UNDERSCORE}{property_name}', new_value)
        else:
            def _get_property(self) -> property_type:
                return getattr(self, f'{UNDERSCORE}{property_name}')

            def _set_property(self, new_value: property_type) -> None:
                check_type(f'{class_.__name__} {property_name}', new_value, property_type)
                setattr(self, f'{UNDERSCORE}{property_name}', new_value)

        getter = property(_get_property)
        setattr(class_, property_name, getter)
        setattr(class_, property_name, getter.setter(_set_property))
        return class_
    return wrapper


def add_simple_list_operations(
    list_name: str,
    elem_name: str,
    elems_type: Type[Any],
) -> Callable:
    """Add "add", "remove" and "get_all" methods to property with list type.

    Args:
        list_name: name of property (list) you want to add methods
        elem_name: name of element in list (e.g., "student" for list_name = students)
        elems_type: type of values that must be in list (property)

    Returns:
        decorator function
    """
    def wrapper(class_: type) -> type:
        full_list_name = f'{class_.__name__} {list_name}'

        def _add(self, new_value: elems_type) -> None:
            check_type(full_list_name, new_value, elems_type)
            elems = getattr(self, f'{UNDERSCORE}{list_name}')
            elems.append(new_value)

        def _remove(self, del_value: elems_type) -> None:
            check_type(full_list_name, del_value, elems_type)
            elems = getattr(self, f'{UNDERSCORE}{list_name}')

            if del_value not in elems:
                raise ValueError(f'{elem_name.title()} ({del_value}) not in {full_list_name}')
            elems.remove(del_value)

        def _get_all(self) -> list[str]:
            return [str(elem) for elem in getattr(self, f'{UNDERSCORE}{list_name}')]

        setattr(class_, f'add{UNDERSCORE}{elem_name}', _add)
        setattr(class_, f'remove{UNDERSCORE}{elem_name}', _remove)
        setattr(class_, f'get_all{UNDERSCORE}{list_name}', _get_all)
        return class_
    return wrapper
