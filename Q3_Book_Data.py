from datetime import datetime

# Sample book data with titles, authors, and checkout status
library_books = [
    {"title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "checked_out": True, "due_date": "2024-09-15"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "checked_out": False, "due_date": None},
    {"title": "The Da Vinci Code", "author": "Dan Brown", "checked_out": True, "due_date": "2024-08-20"},
    {"title": "The Alchemist", "author": "Paulo Coelho", "checked_out": False, "due_date": None},
    {"title": "And Then There Were None", "author": "Agatha Christie", "checked_out": True, "due_date": "2024-09-01"},
]

# Function to calculate the total number of books
def total_books(data):
    """Returns the total number of books in the library."""
    return len(data)

# Function to calculate the total number of books available (not checked out)
def available_books(data):
    """Returns the number of books that are currently available."""
    return sum(1 for book in data if not book["checked_out"])

# Function to list all overdue books
def overdue_books(data):
    """Returns a list of books that are overdue based on today's date."""
    overdue = []
    today = datetime.today().date()  # Get today's date
    for book in data:
        if book["checked_out"] and book["due_date"]:  # Check if the book is checked out and has a due date
            due_date = datetime.strptime(book["due_date"], "%Y-%m-%d").date()  # Convert due date to a date object
            if due_date < today:  # Check if the due date has passed
                overdue.append(book)  # Add to overdue list if the book is overdue
    return overdue

# Function to track the most borrowed books
def most_borrowed_books(data):
    """Returns a list of currently borrowed books sorted by their due date."""
    borrowed = sorted([book for book in data if book["checked_out"]], key=lambda x: x["due_date"])  # Sort borrowed books by due date
    return borrowed

# Running the analysis
total_books_count = total_books(library_books)  # Calculate total number of books
available_books_count = available_books(library_books)  # Calculate available books
overdue_books_list = overdue_books(library_books)  # Get list of overdue books
most_borrowed_books_list = most_borrowed_books(library_books)  # Get list of most borrowed books

# Printing the results
print(f"Total Number of Books: {total_books_count}")  # Print total number of books
print(f"Total Number of Available Books: {available_books_count}")  # Print number of available books

print("\nOverdue Books:")
for book in overdue_books_list:
    print(f"  Title: {book['title']}")
    print(f"  Author: {book['author']}")
    print(f"  Due Date: {book['due_date']}\n")  # Print overdue book details on separate lines

print("Most Borrowed Books:")
for book in most_borrowed_books_list:
    print(f"  Title: {book['title']}")
    print(f"  Author: {book['author']}")
    print(f"  Due Date: {book['due_date']}\n")  # Print most borrowed book details on separate lines
