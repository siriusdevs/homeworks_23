"""This module include class Client."""

from typing import Self


class Client:
    """This class describes Client."""

    def __init__(self, name: str) -> None:
        """Init class Client.

        Args:
            name (str): Name of client
        """
        self.name = name

    @property
    def name(self) -> str:
        """Get name.

        Returns:
            Name of client.
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """Set name.

        Args:
            new_name (str): new client name

        Raises:
            TypeError: if new_name not str
        """
        if not isinstance(new_name, str):
            raise TypeError(f'{new_name} must be str')
        self._name = new_name

    def __repr__(self) -> str:
        """Str represent of the object for debug.

        Returns:
            str:  A string representation of the object.
        """
        return self.name

    def __eq__(self, __value: Self) -> bool:
        """Check equality two object type Client.

        Args:
            __value (Self): object type Client

        Returns:
            bool: equal two object
        """
        if isinstance(__value, Client):
            return self.name == __value.name
        return NotImplemented
