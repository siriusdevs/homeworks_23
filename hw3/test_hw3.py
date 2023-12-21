"""Tests for hw3."""


from hw3 import Book, Librarian, Library, Reader

BOOK_TITLE_ONE = 'The Great Gatsby'
BOOK_AUTHOR_ONE = 'F. Scott Fitzgerald'
BOOK_YEAR_ONE = 1925

BOOK_TITLE_TWO = 'To Kill a Mockingbird'
BOOK_AUTHOR_TWO = 'Harper Lee'
BOOK_YEAR_TWO = 1960

BOOK_TITLE_THREE = '1984'
BOOK_AUTHOR_THREE = 'George Orwell'
BOOK_YEAR_THREE = 1949

BOOK_TITLE_FOUR = 'The Catcher in the Rye'
BOOK_AUTHOR_FOUR = 'J.D. Salinger'
BOOK_YEAR_FOUR = 1951

BOOK_TITLE_FIVE = 'The Hobbit'
BOOK_AUTHOR_FIVE = 'J.R.R. Tolkien'
BOOK_YEAR_FIVE = 1937

READER_NAME_ONE = 'John Doe'
READER_NAME_TWO = 'Jane Doe'
READER_NAME_THREE = 'Bob Johnson'

LIBRARIAN_NAME_ONE = 'Alice Smith'
LIBRARIAN_NAME_TWO = 'Eve Brown'


def test_book_initialization():
    """Test the initialization of the Book class."""
    book = Book(title=BOOK_TITLE_ONE, author=BOOK_AUTHOR_ONE, year=BOOK_YEAR_ONE)
    assert book.title == BOOK_TITLE_ONE
    assert book.author == BOOK_AUTHOR_ONE
    assert book.year == BOOK_YEAR_ONE


def test_book_string_representation():
    """Test the __str__ method of the Book class."""
    book = Book(title=BOOK_TITLE_TWO, author=BOOK_AUTHOR_TWO, year=BOOK_YEAR_TWO)
    assert str(book) == f'{BOOK_TITLE_TWO} by {BOOK_AUTHOR_TWO} ({BOOK_YEAR_TWO})'


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
    book = Book(title=BOOK_TITLE_FOUR, author=BOOK_AUTHOR_FOUR, year=BOOK_YEAR_FOUR)
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


def test_librarian_lend_and_accept_book():
    """Test lending and accepting a book in the Librarian class."""
    library = Library()
    book = Book(title=BOOK_TITLE_FIVE, author=BOOK_AUTHOR_FIVE, year=BOOK_YEAR_FIVE)
    reader = Reader(name=READER_NAME_THREE)
    librarian = Librarian(name=LIBRARIAN_NAME_TWO)

    library.add_book(book)
    librarian.lend_book(reader, library, book)
    assert not library.get_all_books()

    librarian.accept_book(reader, library, book)
    assert library.get_all_books()
