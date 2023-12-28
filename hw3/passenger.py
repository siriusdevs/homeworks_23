"""Module with Passenger class."""

import check_functions as check


class Passenger:
    """A class that describes the passenger with the passenger name and passport number."""

    def __init__(self, passenger_name: str, passport_number: str) -> None:
        """Initialize a Passenger instance.

        Args:
            passenger_name (str): name of the passenger.
            passport_number (str): passport number of the passenger.
        """
        self.passenger_name = passenger_name
        self.passport_number = passport_number

    @property
    def passenger_name(self) -> str:
        """Get fhe passenger_name.

        Returns:
            str: passenger_name.
        """
        return self._passenger_name

    @passenger_name.setter
    def passenger_name(self, new_passenger_name: str) -> None:
        """Set the passenger_name.

        Args:
            new_passenger_name (str): new passenger_name value.
        """
        check.check_passenger_name(new_passenger_name)
        self._passenger_name = new_passenger_name

    @property
    def passport_number(self) -> str:
        """Get fhe passport_number.

        Returns:
            str: passport_number.
        """
        return self._passport_number

    @passport_number.setter
    def passport_number(self, new_passport_number: str) -> None:
        """Set the passport_number.

        Args:
            new_passport_number (str): new passport_number value.
        """
        check.check_passport_number(new_passport_number)
        self._passport_number = new_passport_number
