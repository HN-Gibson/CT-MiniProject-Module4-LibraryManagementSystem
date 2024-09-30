from ErrorHandling import UserInputEmpty
from ErrorHandling import InvalidEntry
from ErrorHandling import BookNotFound
import BookOps

class UserInterface:
    def __init__(self):
        pass
    def main(self):
        while True:
            try:
                print("""
                      Welcome to the Library Management System!

                        Main Menu:
                        1. Book Operations
                        2. User Operations
                        3. Author Operations
                        4. Quit
                      """)
                user_request = input("Please enter the number associated with the operations you would like to access:\n")
                if user_request == "":
                    raise UserInputEmpty
                elif user_request == "1":
                    self.book_operations()
                elif user_request == "2":
                    self.user_operations()
                elif user_request == "3":
                    self.author_operations()
                elif user_request == "4":
                    break
                else:
                    raise InvalidEntry
            except UserInputEmpty:
                UserInputEmpty.handle_user_input_empty()
            except InvalidEntry:
                InvalidEntry.handle_invalid_entry()

    def book_operations(self):
        library = {}
        while True:
            try:
                print("""
                    Book Operations:
                        1. Add a new book
                        2. Borrow a book
                        3. Return a book
                        4. Search for a book
                        5. Display all books
                        6. Return to Main Menu
                      """)
                user_request = input("Please enter the number associated with the operation you would like to perform:\n")
                if user_request == "":
                    raise UserInputEmpty
                elif user_request == "1":     
                    title = input("Enter the title:\n")
                    author = input("Enter the author:\n")
                    genre = input("Enter the genre:\n")
                    pub_date = input("Enter the date of publication:\n")
                    library[title] = BookOps.Book(title,author,genre,pub_date)
                    print (f"'{title}' Added!")
                elif user_request == "2":
                    title = input ("Enter title you would like to borrow:\n")
                    pass
                elif user_request == "3":
                    title = input ("Enter title you would like to return:\n")
                    pass
                elif user_request == "4":
                    title = input ("Enter title you would like to search:\n")
                    book_data = library.get(title)
                    if book_data == None:
                        raise BookNotFound
                    else:
                        print(book_data) 
                elif user_request == "5":
                    if library == {}:
                        print("No books in library!")
                    else:
                        for title in library:
                            print(f"'{title}'")
                elif user_request == "6":
                    break
                else:
                    raise InvalidEntry
            except UserInputEmpty:
                UserInputEmpty.handle_user_input_empty()
            except InvalidEntry:
                InvalidEntry.handle_invalid_entry()
            except BookNotFound:
                BookNotFound.handle_book_not_found()

    def user_operations(self):
        while True:
            try:
                print("""
                    User Operations:
                        1. Add a new user
                        2. View user details
                        3. Display all users
                        4. Return to Main Menu
                      """)
                user_request = input("Please enter the number associated with the operation you would like to perform:\n")
                if user_request == "":
                    raise UserInputEmpty
                elif user_request == "1":
                    pass
                elif user_request == "2":
                    pass
                elif user_request == "3":
                    pass
                elif user_request == "4":
                    break
                else:
                    raise InvalidEntry
            except UserInputEmpty:
                UserInputEmpty.handle_user_input_empty()
            except InvalidEntry:
                InvalidEntry.handle_invalid_entry()

    def author_operations(self):
        while True:
            try:
                print("""
                    Author Operations:
                        1. Add a new author
                        2. View author details
                        3. Display all authors
                        4. Return to Main Menu
                      """)
                user_request = input("Please enter the number associated with the operation you would like to perform:\n")
                if user_request == "":
                    raise UserInputEmpty
                elif user_request == "1":
                    pass
                elif user_request == "2":
                    pass
                elif user_request == "3":
                    pass
                elif user_request == "4":
                    break
                else:
                    raise InvalidEntry
            except UserInputEmpty:
                UserInputEmpty.handle_user_input_empty()
            except InvalidEntry:
                InvalidEntry.handle_invalid_entry()