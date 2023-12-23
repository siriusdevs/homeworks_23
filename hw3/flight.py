"""Module that contains Flight class."""

from . import hw3


class Flight:
    """Class that represents a flight."""

    def __init__(self, flight_num: int, approaching_arirport: str, outcome_airport: str) -> None:
        """Initialize flight.

        Args:
            flight_num (int): flight number
            approaching_arirport (str): arrival point
            outcome_airport (str): departure point
        """
        self.flight_num = flight_num
        self.approaching_arirport = approaching_arirport
        self.outcome_airport = outcome_airport

    @property
    def flight_num(self) -> int:
        """Getter for flight number.

        Returns:
            _flight_num (int): flight number
        """
        return self._flight_num

    @flight_num.setter
    def flight_num(self, new_num: int) -> None:
        """Setter for flight number.

        Args:
            new_num (int): new flight number

        Raises:
            NegativeNumber: when flight number is negative or zero
            InvalidType: when new_num type isn't int
        """
        if not isinstance(new_num, int):
            raise hw3.InvalidType(new_num, int)
        if new_num <= 0:
            raise hw3.NegativeNumber(new_num)
        self._flight_num = new_num

    @property
    def approaching_arirport(self) -> str:
        """Getter for approaching airport.

        Returns:
            _approaching_airport (str): arrival point
        """
        return self._approaching_airport

    @approaching_arirport.setter
    def approaching_arirport(self, approaching_arirport: str) -> None:
        """Setter for approaching airport.

        Args:
            approaching_arirport (str): arrival point

        Raises:
            InvalidType: when approaching_airport type isn't str
        """
        if not isinstance(approaching_arirport, str):
            raise hw3.InvalidType(approaching_arirport, str)
        self._approaching_airport = approaching_arirport

    @property
    def outcome_airport(self) -> str:
        """Getter for outcome airport.

        Returns:
            _outcome_airport (str): departure point
        """
        return self._outcome_airport

    @outcome_airport.setter
    def outcome_airport(self, outcome_airport: str) -> None:
        """Setter for outcome airport.

        Args:
            outcome_airport (str): departure point

        Raises:
            InvalidType: when outcome_airport type isn't str
        """
        if not isinstance(outcome_airport, str):
            raise hw3.InvalidType(outcome_airport, str)
        self._outcome_airport = outcome_airport
