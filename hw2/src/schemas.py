"""Contain msgspec based types and models for hw2."""

from datetime import date
from typing import Annotated

from msgspec import Meta, Struct

MIN_ALLOWED_AGE = 12
MAX_ALLOWED_AGE = 120


AllowedAge = Annotated[float, Meta(ge=MIN_ALLOWED_AGE, le=MAX_ALLOWED_AGE)]


class User(Struct):
    """The msgspec struct representing a valid User model."""

    region: str
    registered: date
    email: str
    age: AllowedAge
    last_login: date


Users = list[User]
