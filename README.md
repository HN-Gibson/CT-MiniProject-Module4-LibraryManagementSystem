# CT-MiniProject-Module4
Presenting a Program for a Library Management System

**Welcome to my Contact Management System.**

**First of all, thank you for using my program!**

**Goal of this Program:** 
This program exists to provide a means of managing the flow of books in and out of a library.
It also provides information regarding the authors featured in the library.

**Important Notes:**
- There are three primary collections in the library that you will access via different menus.
    1. The Library
    2. The User Database
    3. The Author Database
- Throughout the program, you will be given the option to return to the main menu when met with a menu. Please pay attention to the menu options as they are presented.
- The only means of quitting the program is from the main menu. So, when you're finished using the features of one menu, return to the main menu if you would like to exit.
- When navigating the menus, leaving inputs blank (i.e. Hitting enter without typing an input) may result in having to re-enter information.

**Now, to the important how to of my program:**

- When you start the program by running the 'main.py', you will be met with four options. These represent the means of accessing the three primary collections within the program as well as an option to quit the program.

**Note: When using the menus, please make sure you are entering the number associated with the menu option and not the name of that option**

1. Book Operations (a.k.a., 'BookOps')
    - Within this menu, you are able to access the Library to: 
        1. Add books, including information about the author, genre, and year it was published.
            - Note: All newly added books will enter the collection with a designation of available. To change this, use the Borrow a book option to update the status as well as who has the book.
        2. Borrow a book, making note of the user that has it checked out and tieing that information to their User ID.
        3. Return a book, removing the note from a user who has previously been marked as having the book.
        4. Search for a specific book to see it's information, including if it is available.
        5. Display the title of all books in the Library.
            - Note: This option can be used prior to searching to see what is in the library.
        6. Return to Main Menu
    - After completeing an operation, you will have the opporunity to continue accessing other operations in this menu before returning to the main menu.

2. User Operations (a.k.a., 'UserOps')
    -Within this menu, you are able to access the User Database to:
        1. Add users, including a clever or not so clever User ID, which will be used to search for that user later.
        2. View user details, such as name, User ID, and what books they have currently by searching with the associated User ID.
        3. Display all User IDs, allowing you to see all the User IDs.
            -Note: This option can be used prior to searching to see what is in the database.
        4. Return to Main Menu
            - After completeing an operation, you will have the opporunity to continue accessing other operations in this menu before returning to the main menu.

3. Author Operations (a.k.a., 'AuthorOps')
    -Within this menu, you are able to access the Author Database to:
        1. Add authors, including a brief bio.
            - Authors are not automatically added when a book by them is added
        2. View author details, including their name and bio, by seraching using the author's name.
        3. Display all authors, allowing you to see all authors in the system.
            -Note: This option can be used prior to searching to see what is in the database.
        4. Return to Main Menu
            - After completeing an operation, you will have the opporunity to continue accessing other operations in this menu before returning to the main menu.

**A few technical notes**

1. This program uses object oriented programming principles, but this does not mean your data is saved when you exit the program. I hope to implement this feature in the future through file handling.
2. There are seven python files associated with this program:
    - main.py: Run this file to run the program
    - UI.py: This file hosts the classes and methods associated with the menus.
    - LibraryOps.py: This file hosts the primary Library class which acts as a kind of go between for the other classes as well as the instances of the three collections. It is instanced in the UI.py
    - BookOps.py: This file hosts the Book class, allowing books to be created and added as objects to the Library class. 
    - UserOps.py: This file hosts the User class, allowing users to be created and added as objects to the Library class.
    - AuthorOps.py: This file hosts the Author class, allowing authors to be created and added as objects to the Library class.
    - ErrorHandling.py: This file holds various custom Exception classes that are used throughout the other files.
3. Above all else, enjoy my program. Your feedback is critical to my success. I look forward to receiving it!

**Thank you for using my program**