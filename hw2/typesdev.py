"""hw2 module for all custom types."""

UserData = dict[str, str | int]
Users = dict[str, UserData]
UserStats = dict[str, int]

Error = dict[str, str | dict[str, str]]

TestDataItem = tuple[str, str, Users]
