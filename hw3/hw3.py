"""This module encompasses the definition of the Client class."""

from typing import Self


class Client:
    """A representation of an entity - Client."""

    def __init__(self, client_name: str) -> None:
        """Initialize a Client instance.

        Args:
            client_name (str): The name of the client.
        """
        self.client_name = client_name

    @property
    def client_name(self) -> str:
        """Retrieve the name of the client.

        Returns:
            str: The name of the client.
        """
        return self._client_name

    @client_name.setter
    def client_name(self, new_client_name: str) -> None:
        """Update the name of the client.

        Args:
            new_client_name (str): The new name for the client.

        Raises:
            TypeError: If new_client_name is not a string.
        """
        if not isinstance(new_client_name, str):
            raise TypeError(f'{new_client_name} must be a string')
        self._client_name = new_client_name

    def __repr__(self) -> str:
        """Obtain a string representation of the Client object for debugging.

        Returns:
            str: A string representation of the Client object.
        """
        return self.client_name

    def __eq__(self, other: Self) -> bool:
        """Determine whether two Client instances are equivalent.

        Args:
            other (Self): Another object of type Client.

        Returns:
            bool: True if the two objects are considered equal, False otherwise.
        """
        if isinstance(other, Client):
            return self.client_name == other.client_name
        return NotImplemented
