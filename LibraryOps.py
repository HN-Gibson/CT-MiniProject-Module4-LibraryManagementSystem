from BookOps import Book
from ErrorHandling import BookNotFound

class Library:
    def __init__(self):
        self.library = {}
    
    # "LOTR":{"Title":"LOTR","Author":"J.R.R. Tolkien","Genre":"Fantasy","Year of Publication":"1952","Available":"Available"}

    def add_book(self):
        title = input("Enter the title:\n")
        author = input("Enter the author:\n")
        genre = input("Enter the genre:\n")
        pub_date = input("Enter the date of publication:\n")
        self.library[title] = Book(title,author,genre,pub_date)
        print (f"'{title}' Added!")
    
    def search_book(self):
        title = input ("Enter title you would like to search:\n")
        book_data = self.library.get(title)
        if book_data == None:
            raise BookNotFound
        else:
            print(book_data)
    
    def display_books(self):
        if self.library == {}:
            print("No books in library!")
        else:
            for title in self.library:
                print(f"'{title}'")