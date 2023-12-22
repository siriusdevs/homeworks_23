"""Tests for hw3."""


from hw3 import Book, Librarian, Library, Reader

BOOK_TITLE_ONE = 'The Great Gatsby'
BOOK_AUTHOR_ONE = 'F. Scott Fitzgerald'
BOOK_YEAR_ONE = 1925

BOOK_TITLE_TWO = 'To Kill a Mockingbird'
BOOK_AUTHOR_TWO = 'Harper Lee'
BOOK_YEAR_TWO = 1960

BOOK_TITLE_THREE = 'The Catcher in the Rye'
BOOK_AUTHOR_THREE = 'J.D. Salinger'
BOOK_YEAR_THREE = 1951

READER_NAME_ONE = 'John Doe'
READER_NAME_TWO = 'Jane Doe'


LIBRARIAN_NAME_ONE = 'Alice Smith'
LIBRARIAN_NAME_TWO = 'Eve Brown'


def test_book_initialization():
    """Test the initialization of the Book class."""
    book = Book(title=BOOK_TITLE_ONE, author=BOOK_AUTHOR_ONE, year=BOOK_YEAR_ONE)
    assert book.title == BOOK_TITLE_ONE
    assert book.author == BOOK_AUTHOR_ONE
    assert book.year == BOOK_YEAR_ONE


def test_library_initialization():
    """Test the initialization of the Library class."""
    library = Library()
    assert not library.get_all_books()


def test_reader_initialization():
    """Test the initialization of the Reader class."""
    reader = Reader(name=READER_NAME_ONE)
    assert reader.name == READER_NAME_ONE


def test_reader_borrow_and_return_book():
    """Test borrowing and returning a book in the Reader class."""
    library = Library()
    book = Book(title=BOOK_TITLE_THREE, author=BOOK_AUTHOR_THREE, year=BOOK_YEAR_THREE)
    reader = Reader(name=READER_NAME_TWO)

    library.add_book(book)
    reader.borrow_book(library, book)
    assert not library.get_all_books()

    reader.return_book(library, book)
    assert library.get_all_books()


def test_librarian_initialization():
    """Test the initialization of the Librarian class."""
    librarian = Librarian(name=LIBRARIAN_NAME_ONE)
    assert librarian.name == LIBRARIAN_NAME_ONE
