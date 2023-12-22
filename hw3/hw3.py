"""Library module."""


class Book:
    """A class to represent a book."""

    def __init__(self, name: str, author: str, year: int) -> None:
        """
        Initialize a book.

        Parameters:
            name (str): The name of the book.
            author (str): The author of the book.
            year (int): The year of publication of the book.
        """
        self.name, self.author = name, author
        self.year = year

    @property
    def name(self) -> str:
        """
        Return the name of the book.

        Returns:
            str: The name of the book.
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """
        Set the name of the book.

        Parameters:
            new_name (str): The new name of the book.

        Raises:
            TypeError: If the new name is not a string.
        """
        if not isinstance(new_name, str):
            raise TypeError('Name needs to be str, not {0}'.format(new_name.__class__.__name__))
        self._name = new_name

    @property
    def author(self) -> str:
        """
        Return the author of the book.

        Returns:
            str: The author of the book.
        """
        return self._author

    @author.setter
    def author(self, new_author: str) -> None:
        """
        Set the author of the book.

        Parameters:
            new_author (str): The new author of the book.

        Raises:
            TypeError: If the new author is not a string.
        """
        if not isinstance(new_author, str):
            raise TypeError('Name needs to be str, not {0}'.format(new_author.__class__.__name__))
        self._author = new_author

    @property
    def year(self) -> int:
        """
        Return the year of publication of the book.

        Returns:
            int: The year of publication of the book.
        """
        return self._year

    @year.setter
    def year(self, new_year) -> None:
        """
        Set the year of publication of the book.

        Parameters:
            new_year (int): The new year of publication.

        Raises:
            TypeError: If the new year is not an integer.
        """
        if not isinstance(new_year, int):
            raise TypeError('Name needs to be int, not {0}'.format(new_year.__class__.__name__))
        self._year = new_year


class Library:
    """A class to represent a library."""

    def __init__(self, book_list: list[Book]) -> None:
        """
        Initialize a library.

        Parameters:
            book_list (list[Book]): The list of books in the library.
        """
        self.book_list = book_list

    @property
    def book_list(self) -> list:
        """
        Return the list of books in the library.

        Returns:
            list: The list of books in the library.
        """
        return self._book_list

    @book_list.setter
    def book_list(self, new_books: list[Book]) -> None:
        """
        Set the list of books in the library.

        Parameters:
            new_books (list[Book]): The new list of books.
        """
        for book in new_books:
            check_book_type(book)
        self._book_list = new_books

    def delete_book(self, book) -> None:
        """
        Delete a book from the library.

        Parameters:
            book (Book): The book to delete.

        Raises:
            ValueError: If the book is not in the library.
        """
        if book not in self.book_list:
            raise ValueError('The book is not in the Library')
        self.book_list.remove(book)

    def add_book(self, new_book) -> None:
        """
        Add a new book to the library.

        Parameters:
            new_book (Book): The book to add.
        """
        check_book_type(new_book)
        self.book_list.append(new_book)

    def get_books(self) -> list:
        """
        Return the list of books in the library.

        Returns:
            list: The list of books in the library.
        """
        return self.book_list


class Librarian:
    """A class to represent a librarian."""

    def __init__(self, name: str, library: Library) -> None:
        """
        Initialize a librarian.

        Parameters:
            name (str): The name of the librarian.
            library (Library): The library the librarian works at.
        """
        self.name, self.library = name, library

    @property
    def name(self) -> str:
        """
        Return the name of the librarian.

        Returns:
            str: The name of the librarian.
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """
        Set the name of the librarian.

        Parameters:
            new_name (str): The new name of the librarian.

        Raises:
            TypeError: If the new name is not a string.
        """
        if not isinstance(new_name, str):
            raise TypeError('Name needs to be str, not {0}'.format(new_name.__class__.__name__))
        self._name = new_name

    @property
    def library(self) -> Library:
        """
        Return the library the librarian works at.

        Returns:
            Library: The library the librarian works at.
        """
        return self._library

    @library.setter
    def library(self, new_library: Library) -> None:
        """
        Set the library the librarian works at.

        Parameters:
            new_library (Library): The new library the librarian works at.

        Raises:
            TypeError: If the new library is not of the Library type.
        """
        if not isinstance(new_library, Library):
            raise TypeError('Library needs to be Library, not {0}'.format(
                new_library.__class__.__name__,
            ))
        self._library = new_library

    def give_book(self, book: Book) -> Book:
        """
        Give a book to a reader.

        Parameters:
            book (Book): The book to give.

        Returns:
            Book: The book that was given.

        Raises:
            ValueError: If the book is not in the library.
        """
        check_book_type(book)
        if book not in self.library.get_books():
            raise ValueError('Trying to giva a book that is not in the library')

        self.library.delete_book(book)
        return book

    def receive_book(self, book: Book) -> None:
        """
        Receive a book from a reader.

        Parameters:
            book (Book): The book to receive.
        """
        check_book_type(book)
        self.library.add_book(book)


class Reader:
    """A class to represent a reader."""

    books: list[Book] = []

    def __init__(self, name: str) -> None:
        """
        Initialize a reader.

        Parameters:
            name (str): The name of the reader.
        """
        self.name = name

    def take_book(self, book: Book, librarian: Librarian) -> None:
        """
        Take a book from a librarian.

        Parameters:
            book (Book): The book to take.
            librarian (Librarian): The librarian to take the book from.
        """
        check_book_type(book)
        self.books.append(book)
        librarian.give_book(book)

    def return_book(self, book: Book, librarian: Librarian) -> None:
        """
        Return a book to a librarian.

        Parameters:
            book (Book): The book to return.
            librarian (Librarian): The librarian to return the book to.

        Raises:
            ValueError: If the book was not borrowed.
        """
        check_book_type(book)
        if book not in self.books:
            raise ValueError("Trying to return a book that didn't borrow")
        self.books.remove(book)
        librarian.receive_book(book)


def check_book_type(book: Book) -> None:
    """
    Check if a book is of the Book type.

    Parameters:
        book (Book): The book to check.

    Raises:
        TypeError: If the book is not of the Book type.
    """
    if not isinstance(book, Book):
        raise TypeError(
            'A book needs to be of the Book type, not {0}'.format(book.__class__.__name__),
        )
