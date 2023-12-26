"""Main module of library management."""

from typing import Any

UNDERSCORE = '_'
NAME = 'name'
AUTHOR = 'author'
PUBLICATION_DATE = 'publication_date'
BOOKSHELF = 'bookshelf'
BOOKS = 'books'
LIBRARY = 'library'


def _check_type(new_value: Any, classes: tuple[type, ...] | type):
    if not isinstance(new_value, classes):
        value_class = type(new_value).__name__
        classnames = [class_.__name__ for class_ in classes] if isinstance(classes, tuple) \
            else classes.__name__
        raise TypeError(f'{new_value} of {value_class} should be {classnames}')


def _check_types_in_list(new_list: list[Any], classes: tuple[type, ...] | type):
    _check_type(new_list, list)
    for element in new_list:
        _check_type(element, classes)


def _add_property(property_name: str, classes: tuple[type, ...] | type):
    def _wrapper(cls):
        def _setter(self, new_value: Any):
            _check_type(new_value, classes)
            setattr(self, f'{UNDERSCORE}{property_name}', new_value)

        def _getter(self):
            return getattr(self, f'{UNDERSCORE}{property_name}')
        setattr(cls, property_name, property(_getter, _setter))
        return cls
    return _wrapper


def _add_property_list(list_property_name: str, classes: tuple[type, ...] | type):
    def _wrapper(cls):
        def _setter(self, new_list: list[Any]):
            _check_types_in_list(new_list, classes)
            setattr(self, f'{UNDERSCORE}{list_property_name}', new_list)

        def _getter(self):
            return getattr(self, f'{UNDERSCORE}{list_property_name}')
        setattr(cls, list_property_name, property(_getter, _setter))
        return cls
    return _wrapper


@_add_property(NAME, str)
@_add_property(AUTHOR, str)
@_add_property(PUBLICATION_DATE, int)
class Book:
    """Class that represents a book."""

    def __init__(self, name: str, author: str, publication_date: int) -> None:
        """Initialize a book.

        Args:
            name (str): the name of the book.
            author (str): the author of the book.
            publication_date (int): the date when book was pubclicated.
        """
        self.name = name
        self.author = author
        self.publication_date = publication_date

    def __str__(self) -> str:
        """Representation of a book instance in string.

        Returns:
            str: description of the book.
        """
        return f'Book "{self.name}", author: {self.author}, {self.publication_date}'


@_add_property_list(BOOKSHELF, Book)
class Library:
    """Class that represents a library."""

    def __init__(self, bookshelf: list[Book] | None = None) -> None:
        """Initialize a library.

        Args:
            bookshelf (list[Book] | None, optional): list of the available books.
                Defaults to None.
        """
        self._bookshelf = bookshelf if bookshelf is not None else []

    def add(self, book: Book) -> None:
        """Add the book to the list.

        Args:
            book (Book): book instance to add.
        """
        _check_type(book, Book)
        self._bookshelf.append(book)

    def remove(self, book: Book) -> None:
        """Remove the book from the list.

        Args:
            book (Book): book instance to remove.

        Raises:
            ValueError: occurs if the instance is not presented in the list.
        """
        _check_type(book, Book)
        if book not in self._bookshelf:
            raise ValueError(f'There is no {book} in the library')
        self._bookshelf.remove(book)


@_add_property(NAME, str)
@_add_property(LIBRARY, Library)
class Librarian:
    """Class that represents a librarian."""

    def __init__(self, name: str, library: Library) -> None:
        """Initialize a librarian.

        Args:
            name (str): the name of the librarian.
            library (Library): library, where the librarian works.
        """
        self.name = name
        self.library = library

    def give_book(self, book: Book) -> Book:
        """Take a book from library and give it out.

        Args:
            book (Book): book instance to find in library.

        Raises:
            ValueError: occurs if there is no desired book in the library.

        Returns:
            Book: instance of desired book.
        """
        _check_type(book, Book)
        if book not in self.library.bookshelf:
            raise ValueError(f'Has not found book "{book}" in the library')
        self.library.remove(book)
        return book

    def recieve_book(self, book: Book) -> None:
        """Recieve a book from a reader and put it on the shelf.

        Args:
            book (Book): given book instance.
        """
        _check_type(book, Book)
        self.library.add(book)


@_add_property(NAME, str)
@_add_property_list(BOOKS, list[Book])
class Reader:
    """Class that represents a reader."""

    def __init__(self, name: str) -> None:
        """Initialize a reader.

        Args:
            name (str): the name of the reader.
        """
        self.name = name
        self.books: list[Book] = []

    def take_book(self, book: Book, librarian: Librarian) -> None:
        """Take a book from librarian in library.

        Args:
            book (Book): a desired book instance.
            librarian (Librarian): a librarian from the library.
        """
        _check_type(book, Book)
        got = librarian.give_book(book)
        self.books.append(got)

    def return_book(self, book: Book, librarian: Librarian) -> None:
        """Return a book to librarian in library.

        Args:
            book (Book): instance of a book to return.
            librarian (Librarian): a librarian from the library.

        Raises:
            ValueError: occurs if reader does not have given book instance.
        """
        _check_type(book, Book)
        if book not in self.books:
            raise ValueError(f'Reader {self.name} does not have book {book}')
        librarian.recieve_book(book)
        self.books.remove(book)
