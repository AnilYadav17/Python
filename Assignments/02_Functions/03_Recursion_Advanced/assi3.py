'''3.
Cricket Tournament – Highest Run Scorer

A cricket academy wants to reward the player who scored the highest number of runs in a tournament.

Write a Python program to identify the highest run scorer using reduce() and a lambda expression.

Input
players = [
    ("Virat", 78),
    ("Rohit", 102),
    ("Gill", 89),
    ("KL Rahul", 65),
    ("Iyer", 91)
]
Expected Output
Highest Run Scorer: Rohit'''

from functools import reduce

n = int(input("Enter number of Players: "))
players = []
for i in range(n):
    name = input(f"Enter {i+1} Name: ")
    runs = int(input(f"Enter {i+1} Runs: "))
    players.append((name, runs))

ans = reduce(lambda a, b: a if a[1] > b[1] else b, players)
print("Highest Run Scorer:", ans[0])
