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
    with open(DATABASE_FILE,'a') as db_file:
        db_file.write(f"{title},{author}\n")


def search_book(title):
    """
    Search for a book by title.
    :param title: The title of the book to search for
    :return: A dictionary with the book's details if found, else None
    """
    # TODO: Implement logic to search for a book in the database file
    book_details = {}

    with open(DATABASE_FILE) as db_file:
        for line in db_file:
            if title in line.strip():
                details_split = line.split(",")
                book_details['title'] = details_split[0]
                book_details['author'] = details_split[1].strip()
                break

    if book_details:
        return book_details
    else:
        return None

def list_books():
    """
    List all books in the library.
    :return: A list of dictionaries with each book's details
    """
    # TODO: Read all books from the database file and return them as a list of dictionaries
    all_books = []
    with open(DATABASE_FILE) as db_file:
        for line in db_file:
            if line:
                details = line.split(",")
                title = details[0]
                dict = search_book(title)
                if dict is None:
                    pass
                else:
                    all_books.append(dict)
    return all_books
