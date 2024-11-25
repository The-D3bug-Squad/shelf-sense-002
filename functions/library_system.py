DATABASE_FILE = "./database/books.txt"

def initialize_database():
    """
    Initialize the database file if it doesn't exist.
    """
    with open(DATABASE_FILE, 'a') as db:
        pass # Ensure the file exists

def add_book(title, author):
    """
    Add a new book to the library.
    :param title: The title of the book
    :param author: The author of the book
    """
    with open(DATABASE_FILE, 'a') as db:
        db.write(f"{title},{author}")
    print(add_book(title, author))

def search_book(title):
    """
    Search for a book by title.
    :param title: The title of the book to search for
    :return: A dictionary with the book's details if found, else None
    """
    with open(DATABASE_FILE, 'r') as db:
        for words in db:
            book_title, book_author = words.strip().split(',', 1)
            if book_title.lower() == title.lower():
                return {"title": book_title, "author": book_author}
    return None

def list_books():
    """
    List all books in the library.
    :return: A list of dictionaries with each book's details
    """
    books_list = []
    with open(DATABASE_FILE, 'r') as db:
        for words in db:
            book_title, book_author = words.strip().split(',', 1)
            books_list.append({book_title : book_author})
    return books_list
#print(list_books())
