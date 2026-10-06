'''
Question 6: Library Book Management System

A library wants to maintain information about books. The librarian should be able to:

View book details.
Issue the book to a student.
Return the book.
Requirements

Create a class named Book with the following attributes:

book_id
title
author
status (Initially "Available")

Initialize the values using a constructor.

Create the following methods:
display_details() → Displays all book information.
issue_book() → Changes the status to "Issued".
return_book() → Changes the status to "Available".
Sample Input
Enter Book ID : B101
Enter Book Title : Python Programming
Enter Author Name : John Smith
Sample Output
------ Book Details ------
Book ID     : B101
Title       : Python Programming
Author      : John Smith
Status      : Available

Book issued successfully.

------ Book Details ------
Book ID     : B101
Title       : Python Programming
Author      : John Smith
Status      : Issued

Book returned successfully.

------ Book Details ------
Book ID     : B101
Title       : Python Programming
Author      : John Smith
Status      : Available
'''

class Book:

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = "Available"

    def display_details(self):
        print(f"""
------ Book Details ------
Book ID     : {self.book_id}
Title       : {self.title}
Author      : {self.author}
Status      : {self.status}""")

    def issue_book(self):
        if self.status == "Available":
            self.status = "Issued"
            print("\nBook issued successfully.")
        else:
            print("\nBook is already issued.")

    def return_book(self):
        if self.status == "Issued":
            self.status = "Available"
            print("\nBook returned successfully.")
        else:
            print("\nBook is not issued yet.")


book_id = input("Enter Book ID : ")
title = input("Enter Book Title : ")
author = input("Enter Author Name : ")

b1 = Book(book_id, title, author)
b1.display_details()
b1.issue_book()
b1.display_details()
b1.return_book()
b1.display_details()
