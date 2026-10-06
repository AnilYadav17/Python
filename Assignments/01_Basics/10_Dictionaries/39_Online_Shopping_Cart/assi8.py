'''
=========================================
LIBRARY BOOK ISSUE TRACKER
==========================

A library records issued books.

books = [
"Python",
"Java",
"Python",
"C++",
"Java",
"Python"
]

Write a program to:

* Count how many times each book was issued.

Sample Output:
{
'Python':3,
'Java':2,
'C++':1
}
'''

books = [
    "Python",
    "Java",
    "Python",
    "C++",
    "Java",
    "Python"
]

issued_count = {}
for book in books:
    issued_count[book] = issued_count.get(book, 0) + 1

print(issued_count)
