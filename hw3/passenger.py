"""Module that contains Passenger class."""
from . import hw3


class Passenger:
    """Class that represents a passenger."""

    def __init__(self, name: str, passport_id: str) -> None:
        """Initialize passenger.

        Args:
            name (str): passenger name
            passport_id (str): passenger passport id
        """
        self.name = name
        self.passport_id = passport_id

    @property
    def name(self) -> str:
        """Getter for name.

        Returns:
            _name (str): passenger name
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """Setter for name.

        Args:
            new_name (str): new name

        Raises:
            InvalidType: when new_name type isn't str
        """
        if not isinstance(new_name, str):
            raise hw3.InvalidType(new_name, str)
        self._name = new_name

    @property
    def passport_id(self) -> str:
        """Getter for passport id.

        Returns:
            _passport_id (str): passenger passport id
        """
        return self._passport_id

    @passport_id.setter
    def passport_id(self, new_id: str) -> None:
        """Setter for passport id.

        Args:
            new_id (str): new passport id

        Raises:
            InvalidType: when new_id type isn't str
            ValueError: when new_id is not 6 digits string
        """
        if not isinstance(new_id, str):
            raise hw3.InvalidType(new_id, str)
        if len(new_id) != 6:
            raise ValueError('Passport id must be 6 digits, not {0}'.format(len(new_id)))
        if not new_id.isnumeric():
            raise ValueError('Passport id must not contain anything other than numbers')
        self._passport_id = new_id
