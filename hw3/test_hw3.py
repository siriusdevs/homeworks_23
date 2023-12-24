"""Module for testing the main module."""

import pytest

from hw3 import Book, Librarian, Library, Reader

BOOK_NAME = 'A Summer in the Red Scarf'
BOOK_AUTHOR = 'Elena Malisova and Katerina Silvanova'
BOOK_PUBLICATION_DATE = 2021

FAIL_BOOK_NAME = 'Dead Sould'
FAIL_BOOK_AUTHOR = 'Nikolai Gogol'
FAIL_BOOK_PUBLICATION_DATE = 1842

LIBRARIAN_NAME = 'Vladimir'
NEW_LIBRARIAN_NAME = 'Vova'

READER_NAME = 'Yuriy'
NEW_READER_NAME = 'Yurchka'


@pytest.fixture
def book() -> Book:
    """Instantiate and return a book.

    Returns:
        Book: book instance with given name, author and publication date.
    """
    return Book(BOOK_NAME, BOOK_AUTHOR, BOOK_PUBLICATION_DATE)


@pytest.fixture
def failbook() -> Book:
    """Instantiate and return a book used to raise an exception or fail.

    Returns:
        Book: book instance with given name, author and publication date.
    """
    return Book(FAIL_BOOK_NAME, FAIL_BOOK_AUTHOR, FAIL_BOOK_PUBLICATION_DATE)


def test_book_exception() -> None:
    """Asserts that instantiating a book with wrongs args raises an exception."""
    with pytest.raises(TypeError):
        Book([1, 9, 8, 4], 'George Orwell', '2022')

        Book('Peace and War', ['Lion', 'Fat'], '1867')

        Book('Crime and Punishment', 'Fyodor Dostoevskiy', '1337')


@pytest.fixture
def library(book: Book) -> Library:
    """Instantiate and return a library.

    Args:
        book (Book): book in library.

    Returns:
        Library: library instance with list of books.
    """
    return Library([book])


def test_library(library: Library, book: Book) -> None:
    """Asserts that methods of Library class do their job.

    Args:
        library (Library): given library to test.
        book (Book): given book to test with.
    """
    assert library.bookshelf == [book]

    library.remove(book)
    assert not library.bookshelf

    library.add(book)
    assert library.bookshelf == [book]


def test_library_exception(library: Library, book: Book, failbook: Book) -> None:
    """Asserts that methods of Library class raise exceptions.

    Args:
        library (Library): given library to test.
        book (Book): given book to test with.
        failbook (Book): book to test with.
    """
    with pytest.raises(ValueError):
        library.remove(failbook)

    with pytest.raises(TypeError):
        library.bookshelf = ['']

    with pytest.raises(TypeError):
        library.bookshelf = {book, failbook}

    with pytest.raises(TypeError):
        library.bookshelf = 'The Holy Bible'


@pytest.fixture
def librarian(library: Library) -> Librarian:
    """Instantiate and return a librarian in a library.

    Args:
        library (Library): the library where librarian works.

    Returns:
        Librarian: librarian instance working in given library.
    """
    return Librarian(LIBRARIAN_NAME, library)


def test_librarian(librarian: Librarian, library: Library, book: Book) -> None:
    """Asserts that methods of Librarian class do their job.

    Args:
        librarian (Librarian): librarian to test.
        library (Library): library, where librarian works.
        book (Book): book to test with.
    """
    librarian.name = NEW_LIBRARIAN_NAME
    assert librarian.name == NEW_LIBRARIAN_NAME

    assert librarian.library == library

    assert librarian.give_book(book) == book

    librarian.recieve_book(book)
    assert librarian.library.bookshelf == [book]


def test_librarian_exception(librarian: Librarian, book: Book, failbook: Book) -> None:
    """Asserts that methods of Librarian class raise exceptions.

    Args:
        librarian (Librarian): librarian to test.
        book (Book): book to test with.
        failbook (Book): book to test with.
    """
    with pytest.raises(ValueError):
        librarian.give_book(failbook)

    with pytest.raises(TypeError):
        librarian.name = FAIL_BOOK_PUBLICATION_DATE

        librarian.library = book

        librarian.give_book(None)

        librarian.recieve_book(None)


@pytest.fixture
def reader() -> Reader:
    """Instantiate and return a reader.

    Returns:
        Reader: reader instance with given name.
    """
    return Reader(READER_NAME)


def test_reader(reader: Reader, librarian: Librarian, book: Book) -> None:
    """Asserts that methods of Reader class do their job.

    Args:
        reader (Reader): reader to test.
        librarian (Librarian): librarian to test.
        book (Book): book to test with.
    """
    reader.name = NEW_READER_NAME
    assert reader.name == NEW_READER_NAME

    reader.take_book(book, librarian)
    assert reader.books == [book]

    reader.return_book(book, librarian)
    assert not reader.books


def test_reader_exception(reader: Reader, librarian: Librarian, failbook: Book) -> None:
    """Asserts that methods of Reader class raise exceptions.

    Args:
        reader (Reader): reader to test.
        librarian (Librarian): librarian to test.
        failbook (Book): book to test with.
    """
    with pytest.raises(ValueError):
        reader.return_book(failbook, librarian)

    with pytest.raises(TypeError):
        reader.name = [f'{NEW_READER_NAME}']

        reader.books = {failbook}

        reader.return_book(FAIL_BOOK_NAME, librarian)

        reader.take_book(FAIL_BOOK_NAME, librarian)
