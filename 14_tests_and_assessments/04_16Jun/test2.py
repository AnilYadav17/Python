'''2.   3.5 marks

A cricket academy wants to analyze player performance. Each player's information is stored as a tuple.

Tuple Format:

(player_id, player_name, runs_scored)

Requirements:

Read N player records from the user and store them as tuples in a list.
Display all player records.
Find and display the player who scored the highest runs.
Find and display the player who scored the lowest runs.
Calculate and display the total runs scored by all players.
Calculate and display the average runs scored.
Display players who scored more than 50 runs.

Test Case:

Input:

Enter number of players: 5

101 Virat 82
102 Rohit 45
103 Gill 120
104 Hardik 38
105 SKY 76

Expected Output:

All Players:
(101, 'Virat', 82)
(102, 'Rohit', 45)
(103, 'Gill', 120)
(104, 'Hardik', 38)
(105, 'SKY', 76)

Highest Scorer:
(103, 'Gill', 120)

Lowest Scorer:
(104, 'Hardik', 38)

Total Runs:
361

Average Runs:
72.2

Players Scoring More Than 50 Runs:
(101, 'Virat', 82)
(103, 'Gill', 120)
(105, 'SKY', 76)

'''

from collections import namedtuple

n = int(input("Enter Number of Players: "))
p = namedtuple("players",["id","name","score"])

players = []
for i in range(n):
	id = int(input("Enter player ID: "))
	name =input("Enter player Name: ")
	score = int(input("Enter player Score: "))
	players.append(p(id,name,score))

highest = players[0]
lowest = players[0]
total = 0
more_than=[]

print("\n All Players: ")
for i in  range(len(players)):
	print(*players[i])
	total+=players[i].score
	if players[i].score>highest.score:
		highest = players[i]
	if players[i].score<lowest.score:
		lowest = players[i]
	if players[i].score>50:
		more_than.append(players[i].id)

print("\nHighest Scorer: ")
print(*highest)
print("\nLowest Scorer: ")
print(*lowest)

print(f"\nTotal Runs: \n{total}")
print(f"\nAverage Runs: \n{total/n}")

print("\nPlayers Scoring More Than 50 Runs:")
for j in range(len(players)):
	for i in more_than:
		if players[j].id==i:
			print(*players[j])
