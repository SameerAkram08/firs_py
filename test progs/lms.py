class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def print_books(self):
        if self.no_of_books == 0:
            print("No books available in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(book)

    def add_book(self, book_title):
        self.books.append(book_title)
        self.no_of_books += 1
        print(f"Book '{book_title}' added to the library.")

    def get_no_of_books(self):
        return self.no_of_books


# Create a library instance
my_library = Library()

# Print the initial number of books
print("Initial number of books:", my_library.get_no_of_books())

# Add books to the library
my_library.add_book("Book 1")
my_library.add_book("Book 2")
my_library.add_book("Book 3")

# Print all books in the library
my_library.print_books()

# Get the updated number of books
print("Updated number of books:", my_library.get_no_of_books())
