'''Assignment 4:
 Lottery Ticket Verification (Count Occurrences Using Recursion)

A lottery company assigns a unique ticket number to every participant. Before announcing the results, the company wants to determine how many times a lucky digit appears in a ticket number. This helps identify tickets eligible for special bonus rewards.

As a software developer, your task is to write a recursive Python program that counts the number of times a given digit appears in the ticket number.

Task

Write a recursive function to count the occurrences of a given digit in a ticket number.

Input Format
The first line contains an integer representing the Ticket Number.
The second line contains an integer representing the Lucky Digit.
Output Format

Display the number of times the lucky digit appears in the ticket number using the format:

Digit <Lucky Digit> appears <Count> times.
Sample Input
Enter Ticket Number:
1122334412

Enter Lucky Digit:
2
Sample Output
Digit 2 appears 3 times.'''

def count_digit(n, digit):
    if n == 0:
        return 0
    count = 1 if n % 10 == digit else 0
    return count + count_digit(n // 10, digit)

ticket = int(input("Enter Ticket Number:\n"))
lucky_digit = int(input("Enter Lucky Digit:\n"))

if ticket == 0:
    count = 1 if lucky_digit == 0 else 0
else:
    count = count_digit(ticket, lucky_digit)

if count == 1:
    print(f"Digit {lucky_digit} appears {count} time.")
else:
    print(f"Digit {lucky_digit} appears {count} times.")
