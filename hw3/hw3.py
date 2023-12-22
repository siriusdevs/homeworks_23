"""Homework about library management."""


class Book:
    """A class representing a book in a library.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        year (int): The publication year of the book.

    Methods:
        __init__(self, title: str, author: str, year: int) -> None:
            Initializes a new Book instance with the specified title, author, and year.

        __str__(self) -> str:
            Returns a string representation of the book in the format "title by author (year)".

    """

    def __init__(self, title: str, author: str, year: int) -> None:
        """Initialize a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self._title = title
        self._author = author
        self._year = year

    @property
    def title(self) -> str:
        """Get the title of the book.

        Returns:
            str: The title of the book.
        """
        return self._title

    @property
    def author(self) -> str:
        """Get the author of the book.

        Returns:
            str: The author of the book.
        """
        return self._author

    @property
    def year(self) -> int:
        """Get the publication year of the book.

        Returns:
            int: The publication year of the book.
        """
        return self._year

    @title.setter
    def title(self, new_title: str) -> None:
        """Set the title of the book.

        Args:
            new_title (str): New title value to assign to the title variable.
        """
        self._title = new_title

    @author.setter
    def author(self, new_author: str) -> None:
        """Set the author of the book.

        Args:
            new_author (str): New author value to assign to the author variable.
        """
        self._author = new_author

    @year.setter
    def year(self, new_year: int) -> None:
        """Set the publication year of the book.

        Args:
            new_year (int): New year value to assign to the year variable.
        """
        self._year = new_year


class Library:
    """A class representing a library of books.

    Attributes:
        books (list[Book]): The list of books in the library.

    Methods:
        __init__(self) -> None:
            Initializes a new Library instance with an empty list of books.

        add_book(self, book: Book) -> None:
            Adds a book to the library.

        remove_book(self, book: Book) -> None:
            Removes a book from the library.

        get_all_books(self) -> list[Book]:
            Gets a list of all books in the library.

        borrow_book(self, reader: Reader, book: Book) -> None:
            Borrows a book from the library.

        return_book(self, reader: Reader, book: Book) -> None:
            Returns a borrowed book to the library.

    """

    def __init__(self) -> None:
        """Initialize a new Library instance."""
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        """Add a book to the library.

        Args:
            book (Book): The book to be added to the library.
        """
        self.books.append(book)

    def remove_book(self, book: Book) -> None:
        """Remove a book from the library.

        Args:
            book (Book): The book to be removed from the library.

        Raises:
            ValueError: If the specified book is not found in the library.
        """
        if book in self.books:
            self.books.remove(book)
        else:
            raise ValueError('Book not found in the library')

    def get_all_books(self) -> list[Book]:
        """Get a list of all books in the library.

        Returns:
            list[Book]: A list of all books in the library.
        """
        return self.books

    def borrow_book(self, reader: 'Reader', book: Book) -> None:
        """Borrow a book from the library.

        Args:
            reader (Reader): The reader borrowing the book.
            book (Book): The book to be borrowed.

        Raises:
            ValueError: If the specified book is not available in the library.
        """
        if book in self.books:
            self.books.remove(book)
        else:
            raise ValueError('Book not available in the library')

    def return_book(self, reader: 'Reader', book: Book) -> None:
        """Return a borrowed book to the library.

        Args:
            reader (Reader): The reader returning the book.
            book (Book): The book to be returned.
        """
        self.books.append(book)


class Reader:
    """A class representing a reader.

    Attributes:
        name (str): The name of the reader.

    Methods:
        __init__(self, name: str) -> None:
            Initializes a new Reader instance with the specified name.

        borrow_book(self, library: Library, book: Book) -> None:
            Borrows a book from the library.

        return_book(self, library: Library, book: Book) -> None:
            Returns a borrowed book to the library.

    """

    def __init__(self, name: str) -> None:
        """Initialize a new Reader instance.

        Args:
            name (str): The name of the reader.
        """
        self._name = name

    @property
    def name(self) -> str:
        """Get the name of the reader.

        Returns:
            str: The name of the reader.
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """Set the name of the reader.

        Args:
            new_name (str): New name value to assign to the name variable.
        """
        self._name = new_name

    def borrow_book(self, library: Library, book: Book) -> None:
        """Borrow a book from the library.

        Args:
            library (Library): The library from which the book is borrowed.
            book (Book): The book to be borrowed.
        """
        library.borrow_book(self, book)

    def return_book(self, library: Library, book: Book) -> None:
        """Return a borrowed book to the library.

        Args:
            library (Library): The library to which the book is returned.
            book (Book): The book to be returned.
        """
        library.return_book(self, book)


class Librarian:
    """A class representing a librarian.

    Attributes:
        name (str): The name of the librarian.

    Methods:
        __init__(self, name: str) -> None:
            Initializes a new Librarian instance with the specified name.

        lend_book(self, reader: Reader, library: Library, book: Book) -> None:
            Lends a book to a reader.

        accept_book(self, reader: Reader, library: Library, book: Book) -> None:
            Accepts a returned book from a reader.

    """

    def __init__(self, name: str) -> None:
        """Initialize a new Librarian instance.

        Args:
            name (str): The name of the librarian.
        """
        self._name = name

    @property
    def name(self) -> str:
        """Get the name of the librarian.

        Returns:
            str: The name of the librarian.
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """Set the name of the librarian.

        Args:
            new_name (str): New name value to assign to the name variable.
        """
        self._name = new_name
