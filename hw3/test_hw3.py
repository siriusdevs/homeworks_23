"""Tests for the hw3 module."""
import pytest

from hw3 import Book, Librarian, Library, Reader

BOOK_NAME = '1984'
BOOK_AUTHOR = 'George Orwell'
BOOK_YEAR = 1949


@pytest.fixture
def book() -> Book:
    """
    Return a book.

    Returns:
        Book: The book with the name, author and year of publication.
    """
    return Book(BOOK_NAME, BOOK_AUTHOR, BOOK_YEAR)


def test_book_fail():
    """Test the Book class with wrong parameters."""
    with pytest.raises(TypeError):
        Book(1, 2, 3)

    with pytest.raises(TypeError):
        Book(1, '2', 3)

    with pytest.raises(TypeError):
        Book('1', '2', '3')


@pytest.fixture
def library(book: Book) -> Library:
    """
    Return a library.

    Parameters:
        book (Book): The book to add to the library.

    Returns:
        Library: The library with the book in it.
    """
    return Library([book])


def test_library(library: Library, book: Book):
    """
    Test the Library class.

    Parameters:
        library (Library): The library to test with.
        book (Book): The book to test with.
    """
    assert library.get_books() == [book]

    library.delete_book(book)
    assert not library.get_books()

    library.add_book(book)
    assert library.get_books() == [book]


def test_library_fail(library: Library, book: Book):
    """
    Test the Library class with wrong parameters.

    Parameters:
        library (Library): The library to test with.
        book (Book): The book to test with.
    """
    with pytest.raises(TypeError):
        library.book_list = [1, 2, 3]

    with pytest.raises(TypeError):
        library.book_list = [book, 2, 3]


@pytest.fixture
def librarian(library: Library, book: Book) -> Librarian:
    """
    Return a librarian.

    Parameters:
        library (Library): The library to give the librarian.
        book (Book): The book to give the librarian.

    Returns:
        Librarian: The librarian with the library.
    """
    return Librarian('John', library)


def test_librarian(librarian: Librarian, library: Library, book: Book):
    """
    Test the Librarian class.

    Parameters:
        librarian (Librarian): The librarian to test with.
        library (Library): The library to test with.
        book (Book): The book to test with.
    """
    assert librarian.name == 'John'
    assert librarian.library == library

    assert librarian.give_book(book) == book
    assert not librarian.library.book_list

    librarian.receive_book(book)
    assert librarian.library.book_list == [book]


def test_librarian_fail(librarian: Librarian, library: Library, book: Book):
    """
    Test the Librarian class with wrong parameters.

    Parameters:
        librarian (Librarian): The librarian to test with.
        library (Library): The library to test with.
        book (Book): The book to test with.
    """
    with pytest.raises(TypeError):
        librarian.name = 1

        librarian.library = 1

        librarian.give_book(1)

        librarian.receive_book(1)

    with pytest.raises(ValueError):
        librarian.give_book(Book('a', 'b', 1))


def test_reader(book: Book, librarian: Librarian):  # noqa: WPS218
    """
    Test the Reader class.

    Parameters:
        book (Book): The book to test with.
        librarian (Librarian): The librarian to test with.
    """
    reader = Reader('Jack')
    assert reader.name == 'Jack'
    assert not reader.books

    reader.take_book(book, librarian)
    assert reader.books == [book]
    assert not librarian.library.book_list

    reader.return_book(book, librarian)
    assert not reader.books
    assert librarian.library.book_list == [book]


def test_reader_fail(book: Book, librarian: Librarian):
    """
    Test the Reader class with wrong parameters.

    Parameters:
        book (Book): The book to test with.
        librarian (Librarian): The librarian to test with.
    """
    reader = Reader('Jack')
    with pytest.raises(TypeError):
        reader.name = 1

        reader.take_book(1, librarian)

        reader.return_book(1, librarian)

    with pytest.raises(ValueError):
        reader.return_book(book, librarian)
