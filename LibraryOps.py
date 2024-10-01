from BookOps import Book
from UserOps import User
from ErrorHandling import BookNotFound
from ErrorHandling import UserNotFound

class Library:
    def __init__(self):
        self.library = {}

    def check_out_book(self):
        title = input("Enter title you would like to borrow:\n")
        user_id = input("Please enter your User ID:\n")

    def check_in_book(self):
        title = input("Enter title you would like to return:\n")
        user_id = input("Please enter your User ID:\n")
    
    
    def add_book(self):
        title = input("Enter the title:\n")
        author = input("Enter the author:\n")
        genre = input("Enter the genre:\n")
        pub_date = input("Enter the date of publication:\n")
        self.library[title] = Book(title,author,genre,pub_date)
        print (f"'{title}' Added!")
    
    def search_book(self):
        try:
            title = input("Enter title you would like to search:\n")
            book_data = self.library.get(title)
            if book_data == None:
                raise BookNotFound
            else:
                print(book_data)
        except BookNotFound:
            BookNotFound.handle_book_not_found()
    
    def display_books(self):
        if self.library == {}:
            print("No books in library!")
        else:
            for title in self.library:
                print(f"'{title}'")

class UserDatabase:
    def __init__(self):
        self.user_database = {}
    
    def add_user(self):
        name = input("Enter the user's name:\n")
        user_id = input("Create a unique User ID:\n")
        self.user_database[user_id] = User(name,user_id)
        print (f"{name} created a profile with {user_id} as their User ID!")

    def view_user_detail(self):
        try:
            user_id = input("Enter User ID for user you would like details for:\n")
            user_data = self.user_database.get(user_id)
            if user_data == None:
                raise UserNotFound
            else:
                print(user_data)
        except UserNotFound:
            UserNotFound.handle_user_not_found()

    
        