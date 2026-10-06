'''=====================================================================
QUESTION 5: LIBRARY BOOK RECORDS
================================

A library maintains book information using NamedTuple.

Fields:
book_id, title, author, price

Requirements:

1. Read N book records from the user and store them in a list of NamedTuples.

---

2. Display all book details.

---

3. Find and display the most expensive book.

---

4. Search books by author name.

---

5. Calculate and display the average price of all books.

---

Test Case:

Input:
Enter number of books: 4

B101 Python Basics John 450
B102 Java Programming James 550
B103 Data Science John 700
B104 SQL Guide Smith 300

Enter Author Name: John

Expected Output:
Most Expensive Book:
B103 Data Science John 700

Average Book Price:
500.0

Books Written By John:
B101 Python Basics John 450
B103 Data Science John 700
'''

from collections import namedtuple

Book = namedtuple("Books", ["book_id", "title", "author", "price"])

n = int(input("Enter number of books: "))
books = []
for i in range(n):
    print(f"\nEnter Book {i+1} details:")
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    price = int(input("Enter Book Price: "))
    books.append(Book(book_id, title, author, price))

target_author = input("\nEnter Author Name: ")

print("\nMost Expensive Book:")
expensive_book = books[0]
for b in books:
    if b.price > expensive_book.price:
        expensive_book = b
print(*expensive_book)

print("\nAverage Book Price:")
total_price = 0
for b in books:
    total_price += b.price
print(total_price / n)

print(f"\nBooks Written By {target_author}:")
for b in books:
    if b.author.lower() == target_author.lower():
        print(*b)
