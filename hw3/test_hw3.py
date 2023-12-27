"""Module includes tests for the Client class."""
import pytest

from hw3 import Client

names_of_clients = ('Alla', 'Izolda')


@pytest.mark.parametrize('name', names_of_clients)
def test_client_name(name: str) -> None:
    """Check that the client name is set correctly.

    Args:
        name (str): Name of the client.
    """
    client = Client(name)
    assert client.client_name == name


def test_client_invalid_name():
    """Check that setting an invalid client name raises a TypeError."""
    with pytest.raises(TypeError):
        Client(8)
