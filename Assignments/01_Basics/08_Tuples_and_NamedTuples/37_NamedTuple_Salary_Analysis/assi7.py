'''=====================================================================
QUESTION 7: CRICKET PLAYER PERFORMANCE ANALYSIS
==============================================

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

n = int(input("Enter number of players: "))
players = []
for i in range(n):
    print(f"\nEnter Player {i+1} details:")
    player_id = int(input("Enter Player ID: "))
    player_name = input("Enter Player Name: ")
    runs_scored = int(input("Enter Runs Scored: "))
    players.append((player_id, player_name, runs_scored))

print("\nAll Players:")
for p in players:
    print(p)

highest_scorer = players[0]
lowest_scorer = players[0]
total_runs = 0
for p in players:
    if p[2] > highest_scorer[2]:
        highest_scorer = p
    if p[2] < lowest_scorer[2]:
        lowest_scorer = p
    total_runs += p[2]

print("\nHighest Scorer:")
print(highest_scorer)

print("\nLowest Scorer:")
print(lowest_scorer)

print("\nTotal Runs:")
print(total_runs)

print("\nAverage Runs:")
print(total_runs / n)

print("\nPlayers Scoring More Than 50 Runs:")
for p in players:
    if p[2] > 50:
        print(p)
