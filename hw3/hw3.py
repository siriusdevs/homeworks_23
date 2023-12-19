"""Main module of hw3."""
from abc import ABC, abstractmethod
from typing import Callable, Iterable


def ensure(attr: str, funcs: Iterable[Callable]) -> Callable:
    """
    Add property with specified checks to a class.

    Args:
        attr (str): Name of the attribute.
        funcs (Iterable[Callable]): List of functions to check the attribute.

    Returns:
        Callable: Decorator function.
    """
    def add_property(class_name: type) -> type:
        """
        Add property to a class.

        Args:
            class_name (type): Class to which property is added.

        Returns:
            type: Class with added property.
        """
        def getter(self):
            """
            Getter method for the property.

            Args:
                self: self.

            Returns:
                Any: The value of the property.
            """
            return getattr(self, f'_{attr}')

        def setter(self, input_value):
            """
            Setter method for the property.

            Args:
                self: self.
                input_value: The value to set for the property.
            """
            for func in funcs:
                func(input_value)
            setattr(self, f'_{attr}', input_value)

        setattr(class_name, attr, property(getter, setter))
        return class_name
    return add_property


def check_int(input_value):
    """
    Check if the value is an integer.

    Args:
        input_value: Value to be checked.

    Raises:
        TypeError: If the value is not an integer.
    """
    if not isinstance(input_value, int):
        raise TypeError('Value is expected to be int.')


def check_float(input_value):
    """
    Check if the value is an integer or float.

    Args:
        input_value: Value to be checked.

    Raises:
        TypeError: If the value is not an integer or float.
    """
    if not isinstance(input_value, (float, int)):
        raise TypeError('Value is expected to be int or float.')


def check_positive(input_value):
    """
    Check if the value is positive.

    Args:
        input_value: Value to be checked.

    Raises:
        ValueError: If the value is not positive.
    """
    if input_value < 0:
        raise ValueError('Value is expected to be positive.')


def check_str(input_value):
    """
    Check if the value is a string.

    Args:
        input_value: Value to be checked.

    Raises:
        TypeError: If the value is not a string.
    """
    if not isinstance(input_value, str):
        raise TypeError('Name is expected to be str.')


class Memento(ABC):
    """Abstract class representing the Memento pattern."""

    @abstractmethod
    def __init__(self, *args, **kwargs) -> None:
        """
        Initialize Memento object.

        Args:
            args: any argumetns.
            kwargs: any key word argumets.
        """
        self._state = self.__dict__.copy()
        super().__init__(*args, **kwargs)

    def reset_state(self) -> None:
        """Reset the object to its previous state."""
        for attr, input_value in self._get_state().items():
            setattr(self, attr, input_value)

    def _get_state(self) -> dict:
        """
        Get the state of the object.

        Returns:
            dict: Object state.
        """
        return self._state

    def _set_state(self) -> None:
        """Set the state of the object."""
        self._state = self.__dict__.copy()


@ensure('account_number', (check_int, check_positive))
@ensure('balance', (check_float, check_positive))
class BankAccount(Memento, ABC):
    """Abstract class representing a bank account."""

    @abstractmethod
    def __init__(self, account_number: int, balance: int | float) -> None:
        """
        Initialize BankAccount object.

        Args:
            account_number (int): Account number.
            balance (int | float): Initial balance.
        """
        self.account_number, self.balance = account_number, balance
        super().__init__()


@ensure('credit_limit', (check_float, check_positive))
class CurrentAccount(BankAccount):
    """Class representing a current bank account."""

    def __init__(self, account_number: int, balance: int, credit_limit: int | float) -> None:
        """
        Initialize CurrentAccount object.

        Args:
            account_number (int): Account number.
            balance (int): Initial balance.
            credit_limit (int | float): Credit limit.
        """
        self.credit_limit = credit_limit
        super().__init__(account_number, balance)


@ensure('procents', (check_float, check_positive))
class SavingsAccount(BankAccount):
    """Class representing a savings bank account."""

    def __init__(self, account_number: int, balance: int, procents: int | float) -> None:
        """
        Initialize SavingsAccount object.

        Args:
            account_number (int): Account number.
            balance (int): Initial balance.
            procents (int | float): Interest rate.
        """
        self.procents = procents
        super().__init__(account_number, balance)


@ensure('name', (check_str,))
class Client:
    """Class representing a bank client."""

    def __init__(self, name: str, accounts: list[BankAccount] = None) -> None:
        """
        Initialize Client object.

        Args:
            name (str): Client's name.
            accounts (list[BankAccount]): List of bank accounts.
        """
        self.name = name
        self.accounts = accounts or []

    def check_money(self, money):
        try:
            money = float(money)
        except ValueError:
            raise ValueError('Invalid money. Please provide a valid numeric value.')
        if money < 0:
            raise ValueError('Money is expected to be positive.')
        else:
            return money

    def put_money(self, account_number: int, money: int = 0) -> str:
        """
        Deposit money into a specified account.

        Args:
            account_number (int): Account number.
            money (int): Amount of money to deposit.

        Returns:
            success message.
        """
        for account in self.accounts:
            if account.account_number == account_number:
                money = self.check_money(money)
                account.balance += money
                return 'The money was successfully deposited.'
        return 'The account was not found'

    def take_money(self, account_number: int, money: int = 0) -> str:
        """
        Withdraw money from a specified account.

        Args:
            account_number (int): Account number.
            money (int): Amount of money to withdraw.

        Returns:
            success message.
        """
        self.check_money(money)
        for account in self.accounts:
            if account.account_number == account_number:
                try:
                    account.balance -= money
                except ValueError:
                    account.reset_state()
                    return 'The transfer did not take place.'
                return 'The money was successfully withdrawn.'
        return 'The account was not found.'
