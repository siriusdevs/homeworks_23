"""Contains constants and custom json data types."""

UserData = dict[str, str | int]
JsonData = dict[str, UserData]
JsonStats = dict[str, int]

Error = dict[str, str]

SEARCHING_REFERENCES = ('email', 'registered')
