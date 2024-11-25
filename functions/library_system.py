DATABASE_FILE = "test_books.txt"

def initialize_database():
    """
    Initialize the database file if it doesn't exist.
    """
    try:
        with open(DATABASE_FILE, 'a') as db:
            db.write("")  # Ensure the file exists
    except:
        return



def add_book(title, author):
    """
    Add a new book to the library.
    :param title: The title of the book
    :param author: The author of the book
    """
    # TODO: Append the book's title and author to the database file

    data = f'{title},{author}\n'
    with open(DATABASE_FILE, 'a') as db:
            db.write(data)  # Ensure the file exists


# add_book("19855", "George Orwell")
# with open(DATABASE_FILE, 'r') as f:
#             content = f.read()
# print(content)

def search_book(title):
    """
    Search for a book by title.
    :param title: The title of the book to search for
    :return: A dictionary with the book's details if found, else None
    """
    # TODO: Implement logic to search for a book in the database file
    with open(DATABASE_FILE, 'r') as f:
            content = f.readlines()
    for i in content:
        r = i.replace("\n", "").split(",")
        b = i.replace("\n", "").lower().split(",")

        if title.lower() in b:
             return {
                  "title": r[0],
                  "author": r[1]
             }
    return None
# print(search_book("19855"))


def list_books():
    """
    List all books in the library.
    :return: A list of dictionaries with each book's details
    """
    # TODO: Read all books from the database file and return them as a list of dictionaries
    with open(DATABASE_FILE, 'r') as f:
            content = f.readlines()

    l = []
    for i in content:
        r = i.replace("\n", "").split(",")

        l.append({
                "title": r[0],
                "author": r[1]
            }) 

    return l


# print(list_books())