"""Bank Account Management module."""


class Bank_account:
    """Class representing a bank account."""

    def __init__(self, account_number: int, balance: float | int) -> None:
        """
        Initialize a Bank_account object.

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
        """
        if not isinstance(new_number, int):
            raise TypeError(
                f'The account number type must be int, not {type(new_number).__name__}'
            )
        elif len(str(new_number)) != 20:
            raise ValueError(f'The account number len must be 20, not {len(str(new_number))}')
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
        if not isinstance(new_balance, (float, int)):
            raise TypeError(
                f'The balance type must be int or float, not {type(new_balance).__name__}'
            )
        self._balance = new_balance


class Current_account(Bank_account):
    """Class representing a current bank account."""

    def __init__(
        self,
        account_number: int,
        balance: float | int,
        credit_limit: float | int
    ) -> None:
        """
        Initialize a Current_account object.

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
        """
        if not isinstance(new_limit, (float, int)):
            raise TypeError(
                f'The credit limit must be int or float, not {type(new_limit).__name__}'
            )
        elif new_limit < 0:
            raise ValueError("The credit limit mustn't be negative")
        self._credit_limit = new_limit


class Deposit_account(Bank_account):
    """Class representing a deposit bank account."""

    def __init__(
        self,
        account_number: int,
        balance: float | int,
        interest_rate: float | int
    ) -> None:
        """
        Initialize a Deposit_account object.

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
        """
        if not isinstance(new_rate, (float, int)):
            raise TypeError(
                f'The interest rate must be int or float, not {type(new_rate).__name__}'
            )
        elif new_rate < 0:
            raise ValueError("The interest rate mustn't be negative")
        self._interest_rate = new_rate


class Client:
    """Class representing a bank's client."""

    def __init__(
        self,
        name: str,
        accounts: list[Bank_account]
    ) -> None:
        """
        Initialize a Client object.

        Args:
            name (str): The name of the client.
            accounts (list[Bank_account]): The list of the client's bank accounts.
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
        """
        if not isinstance(new_name, str):
            raise TypeError(f'The name type must be str, not {type(new_name).__name__}')
        elif len(new_name) > 1478:
            raise ValueError('The name len exceeds 1478 characters')
        self._name = new_name

    @property
    def accounts(self) -> list[Bank_account]:
        """
        Return the client's bank accounts.

        Returns:
            list[Bank_account]: The client's bank accounts.
        """
        return self._accounts

    @accounts.setter
    def accounts(self, new_accounts: list[Bank_account]) -> None:
        """
        Set the client's bank accounts.

        Args:
            new_accounts (list[Bank_account]): The client's bank accounts.
        """
        for account in new_accounts:
            if not isinstance(account, (Current_account, Deposit_account)):
                raise TypeError(
                    f'All accounts must be inherited from Bank_account,'
                    f' not {type(account).__name__}'
                )
        self._accounts = new_accounts

    def get_account(self, account_number: int, money: float):
        """
        Checks the transaction for the possibility of execution
        and returns the index of the account in the list.

        Args:
            account_number (int): The number of the client's bank account.
            money (float): Amount of money.

        Returns:
            int: The index of the account in the list of the client's bank accounts.
        """
        if not isinstance(account_number, int):
            raise TypeError(
                f'The account id type must be int, not {type(account_number).__name__}'
            )
        account_id = [
            index for index, account in self.accounts
            if account_number == account.account_number
        ]
        if not account_id:
            raise ValueError('No such id was found')
        elif not isinstance(money, float):
            raise TypeError(f'The money type must be float, not {type(money).__name__}')
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
        """
        account_id = self.get_account(account_number, money)
        account = self.accounts[account_id]
        reserve = account.interest_rate if isinstance(account, Deposit_account) else 0

        if money > account.balance + reserve:
            raise ValueError(
                f'На вашем балансе недостаточно средств!'
                f'Максимальная сумма {account.balance + reserve}'
            )

        self.accounts[account_id].balance -= money
