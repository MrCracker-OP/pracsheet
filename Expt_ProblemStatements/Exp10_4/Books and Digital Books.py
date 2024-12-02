# Base class: Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # Method to return book's info
    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}"

# Derived class: EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Initialize title and author from the base class
        self.file_size = file_size  # Additional attribute for EBook

    # Override get_info method to include file size
    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}, File Size: {self.file_size} MB"

# Example usage
book = Book("The Great Gatsby", "F. Scott Fitzgerald")
ebook = EBook("1984", "George Orwell", 2)

# Printing book details
print(book.get_info())   # Output: Title: The Great Gatsby, Author: F. Scott Fitzgerald
print(ebook.get_info())  # Output: Title: 1984, Author: George Orwell, File Size: 2 MB
