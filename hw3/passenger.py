"""Module that provides the Passenger class."""


from . import hw3


class Passenger:
    """Class for denoting an avia passenger."""

    def __init__(self, name: str, passport_num: str) -> None:
        """Initialize a passenger.

        Args:
            name (str): full name
            passport_num (str): 6 digits
        """
        self.name = name
        self.passport_num = passport_num

    @property
    def name(self) -> str:
        """Get name.

        Returns:
            str: passenger's name
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """Set name.

        Args:
            new_name (str): new name of the passenger
        """
        hw3.check_type(new_name, str)
        self._name = new_name

    @property
    def passport_num(self) -> str:
        """Get passport number.

        Returns:
            str: passenger's passport number
        """
        return self._passport_num

    @passport_num.setter
    def passport_num(self, passport_num: str) -> None:
        """Set passport number.

        Args:
            passport_num (str): 6 digits

        Raises:
            ValueError: when passport_num is not a 6 digits string
        """
        hw3.check_type(passport_num, str)
        if len(passport_num) != 6:
            raise ValueError(f'passport num must have 6 characters, got {passport_num}')
        if not all(char.isdigit() for char in passport_num):
            raise ValueError(f'passport num characters must all be digits, but got {passport_num}')
        self._passport_num = passport_num
