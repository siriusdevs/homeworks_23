"""Contain all the custom built-in based (bb) types for hw2."""

UserData = dict[str, str | int]
Users = dict[str, UserData]
UserStats = dict[str, int]

Error = dict[str, str | dict[str, str]]

TestDataItem = tuple[str, str, Users]
