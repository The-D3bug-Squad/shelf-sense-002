DATABASE_FILE = "./database/books.txt"

def initialize_database():
    """
    Initialize the database file if it doesn't exist.
    """
    with open(DATABASE_FILE, 'a') as db:
        contents = db.readline() # Ensure the file exists

def add_book(title, author):
    """
    Add a new book to the library.
    :param title: The title of the book
    :param author: The author of the book
    """
    
    x = 'Harper'
    if x in contents.items():
        contents.append(x)
    else:
        print('book cannot be added')
        # TODO: Append the book's title and author to the database file

def search_book(title):
    """
    Search for a book by title.
    :param title: The title of the book to search for
    :return: A dictionary with the book's details if found, else None
    """
    for title,author in contents.items():
        if author == 'Harper Lee':
            return title
        elif author == 'George Orwell':
            return title


    # TODO: Implement logic to search for a book in the database file

def list_books():
    """
    List all books in the library.
    :return: A list of dictionaries with each book's details
    """
    
    print("done")
     

    # TODO: Read all books from the database file and return them as a list of dictionaries
