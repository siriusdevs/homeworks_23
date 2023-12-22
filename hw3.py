"""Bank Account Management module."""
from typing import Any


def check_type(
    input_object: Any,
    types: tuple[type, ...] | type,
    object_name: str = 'object',
) -> None:
    """
    Check if the input_object is of type `types`.

    Args:
        input_object (Any): The value to check.
        types (tuple[type, ...]): The type to check against.
        object_name (str): Object name.

    Raises:
        TypeError: If value is not of type `types`.
    """
    if not isinstance(input_object, types):
        value_type = type(input_object)
        error_msg = f'The {object_name} type must be {types}, not {value_type}'
        raise TypeError(error_msg)


class BankAccount:
    """Class representing a bank account."""

    _account_number_len = 20

    def __init__(self, account_number: int, balance: float | int) -> None:
        """
        Initialize a BankAccount object.

        Args:
            account_number (int): The number of the bank account.
            balance (float | int): The balance of the client's bank account.
        """
        self.account_number = account_number
        self.balance = balance

    @property
    def account_number(self) -> int:
        """
        Return the number of the bank account.

        Returns:
            int: The number of the bank account.
        """
        return self._account_number

    @account_number.setter
    def account_number(self, new_number: int) -> None:
        """
        Set the number of the bank account.

        Args:
            new_number (int): The number of the bank account.

        Raises:
            ValueError: If account number len does not match the value of _account_number_len.
        """
        check_type(new_number, int, 'account number')
        number_len = len(str(new_number))
        if number_len != self._account_number_len:
            raise ValueError(
                f'The account number len must be {self._account_number_len}, not {number_len}',
            )
        self._account_number = new_number

    @property
    def balance(self) -> float | int:
        """
        Return the balance of the client's bank account.

        Returns:
            float | int: The balance of the client's bank account.
        """
        return self._balance

    @balance.setter
    def balance(self, new_balance: float | int) -> None:
        """
        Set the balance of the client's bank account.

        Args:
            new_balance (float | int): The balance of the client's bank account.
        """
        check_type(new_balance, (float, int), 'balance')
        self._balance = new_balance


class CurrentAccount(BankAccount):
    """Class representing a current bank account."""

    def __init__(
        self,
        account_number: int,
        balance: float | int,
        credit_limit: float | int,
    ) -> None:
        """
        Initialize a CurrentAccount object.

        Args:
            account_number (int): The number of the bank account.
            balance (float | int): The balance of the client's bank account.
            credit_limit (float | int): The credit limit on the bank account.
        """
        super().__init__(account_number, balance)
        self.credit_limit = credit_limit

    @property
    def credit_limit(self) -> float | int:
        """
        Return the credit limit on the bank account.

        Returns:
            float | int: The credit limit on the bank account.
        """
        return self._credit_limit

    @credit_limit.setter
    def credit_limit(self, new_limit: float | int) -> None:
        """
        Set the credit limit on the bank account.

        Args:
            new_limit (float | int): The credit limit on the bank account.

        Raises:
            ValueError: If credit limit is negative.
        """
        check_type(new_limit, (float, int), 'credit limit')
        if new_limit < 0:
            raise ValueError("The credit limit mustn't be negative")
        self._credit_limit = new_limit


class DepositAccount(BankAccount):
    """Class representing a deposit bank account."""

    def __init__(
        self,
        account_number: int,
        balance: float | int,
        interest_rate: float | int,
    ) -> None:
        """
        Initialize a DepositAccount object.

        Args:
            account_number (int): The number of the bank account.
            balance (float | int): The balance of the client's bank account.
            interest_rate (float | int): The interest rate on the deposit.
        """
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    @property
    def interest_rate(self) -> float | int:
        """
        Return the interest rate on the deposit.

        Returns:
            float | int: The interest rate on the deposit.
        """
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, new_rate: float | int) -> None:
        """
        Set the interest rate of the deposit account.

        Args:
            new_rate (float | int): The interest rate on the deposit.

        Raises:
            ValueError: If interest rate is negative.
        """
        check_type(new_rate, (float, int), 'interest rate')
        if new_rate < 0:
            raise ValueError("The interest rate mustn't be negative")
        self._interest_rate = new_rate


class Client:
    """Class representing a bank's client."""

    _name_len = 1478

    def __init__(
        self,
        name: str,
        accounts: list[BankAccount],
    ) -> None:
        """
        Initialize a Client object.

        Args:
            name (str): The name of the client.
            accounts (list[BankAccount]): The list of the client's bank accounts.
        """
        self.name = name
        self.accounts = accounts

    @property
    def name(self) -> str:
        """
        Return the name of the person.

        Returns:
            str: The name of the person.
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """
        Set the name of the person.

        Args:
            new_name (str): The name of the person.

        Raises:
            ValueError: If the name length exceeds the _name_len value.
        """
        check_type(new_name, str, 'name')
        if len(new_name) > self._name_len:
            raise ValueError(f'The name len exceeds {self.name_len} characters')
        self._name = new_name

    @property
    def accounts(self) -> list[BankAccount]:
        """
        Return the client's bank accounts.

        Returns:
            list[BankAccount]: The client's bank accounts.
        """
        return self._accounts

    @accounts.setter
    def accounts(self, new_accounts: list[BankAccount]) -> None:
        """
        Set the client's bank accounts.

        Args:
            new_accounts (list[BankAccount]): The client's bank accounts.
        """
        for account in new_accounts:
            check_type(account, (CurrentAccount, DepositAccount), 'accounts')
        self._accounts = new_accounts

    def get_account(self, account_number: int, money: float):
        """
        Find the index of the account in the list.

        Args:
            account_number (int): The number of the client's bank account.
            money (float): Amount of money.

        Returns:
            int: The index of the account in the list of the client's bank accounts.

        Raises:
            ValueError: If the amount of money is negative or account id wasn't found.
        """
        check_type(account_number, int, 'account id')
        account_id = [
            index for index, account in self.accounts if account_number == account.account_number
        ]
        check_type(money, float, 'money')
        if not account_id:
            raise ValueError('No such id was found')
        elif money <= 0:
            raise ValueError('Amount of money must be positive number')
        return account_id[0]

    def deposit_money(self, account_number: int, money: float):
        """
        Deposits money to the user's bank account.

        Args:
            account_number (int): The number of the client's bank account.
            money (float): The amount of money to deposit.
        """
        account_id = self.get_account(account_number, money)
        self.accounts[account_id].balance += money

    def withdraw_money(self, account_number: int, money: float):
        """
        Withdraws money from the user's bank account.

        Args:
            account_number (int): The number of the client's bank account.
            money (float): The amount of money to withdraw.

        Raises:
            ValueError: If there are not enough funds on the balance.
        """
        account_id = self.get_account(account_number, money)
        account = self.accounts[account_id]
        available_money = account.interest_rate if isinstance(account, DepositAccount) else 0
        available_money += account.balance

        if money > available_money:
            raise ValueError(
                f'There are not enough funds on the balance ({available_money}).',
            )

        self.accounts[account_id].balance -= money
