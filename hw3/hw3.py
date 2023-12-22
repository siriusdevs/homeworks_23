"""Main module of hw3."""
from abc import ABC, abstractmethod

import module_hw3


def check_bank(input_value: list):
    """
    Check if the input_value is a list and his value is BankAccount.

    Args:
        input_value: Value to be checked.

    Raises:
        TypeError: If the input_value is not list.
        TypeError: If the value is not BankAccount.
    """
    if not isinstance(input_value, list):
        raise TypeError('Bank accounts should be list')
    for account in input_value:
        if not isinstance(account, BankAccount):
            raise TypeError('Your bank account is not instance Bank Account')


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


@module_hw3.ensure('account_number', (module_hw3.check_int, module_hw3.check_positive))
@module_hw3.ensure('balance', (module_hw3.check_float, module_hw3.check_positive))
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


@module_hw3.ensure('credit_limit', (module_hw3.check_float, module_hw3.check_positive))
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


@module_hw3.ensure('procents', (module_hw3.check_float, module_hw3.check_positive))
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


@module_hw3.ensure('accounts', (check_bank,))
@module_hw3.ensure('name', (module_hw3.check_str,))
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
        """
        Check and convert the input to a valid numeric value.

        Args:
            money: The input value to check.

        Returns:
            float: The valid numeric value.

        Raises:
            ValueError: If the input is not a valid numeric value or if it's negative.
        """
        try:
            money = float(money)
        except ValueError:
            raise ValueError('Invalid money. Please provide a valid numeric value.')
        if money < 0:
            raise ValueError('Money is expected to be positive.')
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
