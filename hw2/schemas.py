"""hw2 module for msgspec models and based types."""

from typing import Annotated

from msgspec import Meta, Struct

PossibleAge = Annotated[float, Meta(ge=10)]


class UserDataSchema(Struct):
    """The msgspec struct that represents correct User model."""

    region: str
    registered: str
    email: str
    age: PossibleAge
    last_login: str


UsersSchema = dict[str, UserDataSchema]
