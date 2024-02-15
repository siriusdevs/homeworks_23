"""HW3 task."""


class BankAccount:
    """Bank instance."""

    def __init__(self, account_number: str, balance: float):
        """Bank initialisation.

        Args:
            account_number (str): Account number
            balance (float): balance
        """
        self.account_number = account_number
        self.balance = balance

    @property
    def account_number(self) -> str:
        """Getter of account number of the instance.

        Returns:
            str: account number
        """
        return self._account_number

    @account_number.setter
    def account_number(self, new_account_number: str) -> None:
        """Setter of account number of the intance.

        Args:
            new_account_number (str): new account number

        Raises:
            TypeError: if wrong type
        """
        if not isinstance(new_account_number, str):
            raise TypeError('Your account number must be str')
        self._account_number = new_account_number

    @property
    def balance(self) -> float:
        """Getter of balance of the instance.

        Returns:
            float: balance
        """
        return self._balance

    @balance.setter
    def balance(self, new_balance: float) -> None:
        """Setter of balance of the intance.

        Args:
            new_balance (float): new balance

        Raises:
            TypeError: if wrong type
        """
        if not isinstance(new_balance, float):
            raise TypeError('Your balance should be float')
        self._balance = new_balance


class CheckingAccount(BankAccount):
    """Checks Account instance."""

    def __init__(self, account_number: str, balance: float, credit_limit: float):
        """Represent a checking account.

        Args:
            account_number (str): Account number.
            balance (float): Balance.
            credit_limit (float): Credit limit.
        """
        super().__init__(account_number, balance)
        self.credit_limit = credit_limit

    @property
    def credit_limit(self) -> float:
        """Getter of credit limit of the instance.

        Returns:
            float: Credit limit
        """
        return self._credit_limit

    @credit_limit.setter
    def credit_limit(self, new_credit_limit: float) -> None:
        """Setter of credit limit of the instance.

        Args:
            new_credit_limit (float): ew credit limit

        Raises:
            TypeError: if wrong type
        """
        if not isinstance(new_credit_limit, float):
            raise TypeError('Credit limit should be float')
        self._credit_limit = new_credit_limit


class SavingsAccount(BankAccount):
    """Savings Account instance."""

    def __init__(self, account_number: str, balance: float, interest_rate: float):
        """Initialize a savings account.

        Args:
            account_number (str): The account number.
            balance (float): The balance.
            interest_rate (float): The interest rate.
        """
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    @property
    def interest_rate(self) -> float:
        """Getter of interest rate of the instance.

        Returns:
            float: Interest rate
        """
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, new_interest_rate: float) -> None:
        """Setter of interest rate of the instance.

        Args:
            new_interest_rate (float): New interest rate.

        Raises:
            TypeError: if wrong type
        """
        if not isinstance(new_interest_rate, float):
            raise TypeError('interest rate should be float')
        self._interest_rate = new_interest_rate


class Client:
    """Client instance."""

    def __init__(self, name: str, accounts: list[BankAccount]):
        """Client initialization.

        Args:
            name (str): Name of the client.
            accounts (list[BankAccount]): List of bank accounts associated with the client.
        """
        self.name = name
        self.accounts = accounts

    @property
    def name(self) -> str:
        """Getter of the name of the instance.

        Returns:
            str: Name of the client.
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """Setter of the name of the instance.

        Args:
            new_name (str): New name of the client.

        Raises:
            TypeError: if wrong type
        """
        if not isinstance(new_name, str):
            raise TypeError('Name should be str')
        self._name = new_name

    def withdraw(self, account_number: str, amount: float) -> bool:
        """Withdraw funds from a specified bank account.

        Args:
            account_number (str): Account number from which to withdraw funds.
            amount (float): Amount to withdraw.

        Returns:
            bool: True if the withdrawal is successful, False otherwise.
        """
        for account in self.accounts:
            if account.account_number == account_number:
                if isinstance(account, CheckingAccount):
                    available_balance = account.balance + account.credit_limit
                else:
                    available_balance = account.balance

                if amount <= available_balance:
                    account.balance -= amount
                    return True
        return False

    def deposit(self, account_number: str, amount: float) -> bool:
        """Deposit funds into a specified bank account.

        Args:
            account_number (str): Account number into which to deposit funds.
            amount (float): Amount to deposit.

        Returns:
            bool: True if the deposit is successful, False otherwise.
        """
        for account in self.accounts:
            if account.account_number == account_number:
                account.balance += amount
                return True
        return False
