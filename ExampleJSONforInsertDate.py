import json

def insert_book():
    books = []  # List to store books

    # Ask the user for book details
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    year = input("Enter the publication year: ")

    # Create a dictionary with the book's information
    book = {
        'Title': title,
        'Author': author,
        'Year': year
    }

    try:
        with open('books.json', 'r') as file:
            books = json.load(file)  # Load existing data from the JSON file if any
    except FileNotFoundError:
        pass  # If the file doesn't exist, create a new one

    books.append(book)  # Add the new book to the list

    # Save the updated list to the JSON file
    with open('books.json', 'w') as file:
        json.dump(books, file, indent=4)

    print("Book inserted successfully.")

if __name__ == "__main__":
    insert_book()
