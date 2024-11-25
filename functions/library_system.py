DATABASE_FILE = "test_books.txt"

def initialize_database():
    """
    Initialize the database file if it doesn't exist.
    """
    with open(DATABASE_FILE, 'a') as db:
        pass  # Ensure the file exists

def add_book(title, author):
    """
    Add a new book to the library.
    :param title: The title of the book
    :param author: The author of the book
    """
    # TODO: Append the book's title and author to the database file

    add_book("1984", "George Orwell")
    new_book = {
        'title': title,
        'author': author
    }
    library.append(new_book)
    
    print(f"Book {title}  by {author} has been added to the library.")



def search_book(title):
    """
    Search for a book by title.
    :param title: The title of the book to search for
    :return: A dictionary with the book's details if found, else None
    """
    # TODO: Implement logic to search for a book in the database file

    library = []
    for book in library:
        if book [title].lower() == title.lower():
            return book
        else:
            return None


def list_books():
    """
    List all books in the library.
    :return: A list of dictionaries with each book's details
    """
    # TODO: Read all books from the database file and return them as a list of dictionaries

    books = []
    try:
        with open(DATABASE_FILE, 'r') as file:
            for line in file:
                title, author = line.strip().split(", ")
                book = {
                    "title": title,
                    "author": author
                }
                books.append(book)
        
        return books

    except FileNotFoundError:
        print("The file 'DATABASE_FILE' was not found")
        return []












