import os

DATABASE_FILE = "./database/books.txt"

def initialize_database():
    """
    Initialize the database file if it doesn't exist.
    """
    if not os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, 'a') as db:
            db.write("")



def add_book(title, author):
    """
    Add a new book to the library.
    :param title: The title of the book
    :param author: The author of the book
    """
    try:
        with open(DATABASE_FILE, 'a') as db:
            db.write(f"{title},{author}")
    except FileNotFoundError:
        raise FileNotFoundError(f"{DATABASE_FILE} doesn't exist")
    

def search_book(title):
    """
    Search for a book by title.
    :param title: The title of the book to search for
    :return: A dictionary with the book's details if found, else None
    """
    try:
        with open(DATABASE_FILE, 'r') as db:
            books = db.readlines()
            books = {line.strip().split(",")[0]: line.strip().split(",")[1] for line in books if len(line.strip()) > 0}
    except FileNotFoundError:
        raise FileNotFoundError(f"Database doesn't exist at {DATABASE_FILE}")
    
    return {'title':title, 'author':books[title]} if title in books else None

def list_books():
    """
    List all books in the library.
    :return: A list of dictionaries with each book's details
    """
    try:
        with open(DATABASE_FILE, "r") as db:
            books = db.readlines()
            books = [(line.strip().split(",")[0], line.strip().split(",")[1]) for line in books]
    except FileNotFoundError:
        raise FileNotFoundError(f"Database doesn't exist at {DATABASE_FILE}")
    
    return [{'title': book[0], 'author': book[1]} for book in books if book[0].lower() != 'title']

