"""Tests for hw3."""


from hw3 import Book, Librarian, Library, Reader

BOOK_TITLE = 'The Great Gatsby'
BOOK_AUTHOR = 'F. Scott Fitzgerald'
BOOK_YEAR = 1925
READER_NAME = 'John Doe'
LIBRARIAN_NAME = 'Alice Smith'


def test_book_initialization():
    """Test the initialization of the Book class."""
    book = Book(BOOK_TITLE, BOOK_AUTHOR, BOOK_YEAR)
    assert book.title == BOOK_TITLE
    assert book.author == BOOK_AUTHOR
    assert book.year == BOOK_YEAR


def test_library_initialization():
    """Test the initialization of the Library class."""
    library = Library()
    assert not library.get_all_books()


def test_reader_initialization():
    """Test the initialization of the Reader class."""
    reader = Reader(READER_NAME)
    assert reader.name == READER_NAME


def test_librarian_initialization():
    """Test the initialization of the Librarian class."""
    library = Library()
    book = Book(BOOK_TITLE, BOOK_AUTHOR, BOOK_YEAR)
    library.add_book(book)
    librarian = Librarian(LIBRARIAN_NAME, library)
    assert librarian.name == LIBRARIAN_NAME


def test_reader_borrow_book():
    """Test borrow book of the Reader class."""
    library = Library()
    book = Book(BOOK_TITLE, BOOK_AUTHOR, BOOK_YEAR)
    library.add_book(book)
    librarian = Librarian(LIBRARIAN_NAME, library)
    reader = Reader(READER_NAME)
    librarian.lend_book(reader, book)
    assert not library.get_all_books()


def test_reader_return_book():
    """Test return book of the Reader class."""
    library = Library()
    book = Book(BOOK_TITLE, BOOK_AUTHOR, BOOK_YEAR)
    library.add_book(book)
    librarian = Librarian(LIBRARIAN_NAME, library)
    reader = Reader(READER_NAME)
    librarian.lend_book(reader, book)
    reader.return_book(librarian, book)
    assert (book in library.get_all_books())
