class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True  # Book is available by default

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {'Available' if self.available else 'Not Available'}"


class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.membership_id = membership_id
        self.borrowed_books = []  # List of borrowed books

    def borrow_book(self, book):
        if book.available:
            self.borrowed_books.append(book)
            book.available = False
            print(f"{self.name} borrowed {book.title}.")
        else:
            print(f"{book.title} is currently not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True
            print(f"{self.name} returned {book.title}.")
        else:
            print(f"{self.name} did not borrow {book.title}.")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"Borrowed books by {self.name}:")
            for book in self.borrowed_books:
                print(f"- {book.title}")
        else:
            print(f"{self.name} has not borrowed any books.")


class Library:
    def __init__(self):
        self.books = []  # Collection of books
        self.members = []  # List of library members

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book.title}")

    def register_member(self, member):
        self.members.append(member)
        print(f"Registered member: {member.name}")

    def list_available_books(self):
        available_books = [book for book in self.books if book.available]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f"- {book.title} by {book.author}")
        else:
            print("No available books.")

    def list_borrowed_books_by_member(self, member):
        member.list_borrowed_books()


# Example usage:
if __name__ == "__main__":
    library = Library()

    # Adding books to the library
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
    book2 = Book("1984", "George Orwell", "9780451524935")
    library.add_book(book1)
    library.add_book(book2)

    # Registering members
    member1 = Member("Alice", "M001")
    member2 = Member("Bob", "M002")
    library.register_member(member1)
    library.register_member(member2)

    # Member borrows a book
    member1.borrow_book(book1)

    # Listing available books
    library.list_available_books()

    # Listing borrowed books by a member
    library.list_borrowed_books_by_member(member1)

    # Member returns a book
    member1.return_book(book1)

    # Listing available books again
    library.list_available_books()
