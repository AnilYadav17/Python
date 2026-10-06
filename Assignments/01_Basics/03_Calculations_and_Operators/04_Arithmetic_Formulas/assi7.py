'''Assignment 7: Cricket Run Rate

In cricket, overs are given in decimal format (e.g., 48.3 means 48 overs and 3 balls). Convert overs into total balls and calculate run rate.

Input:
Total runs = 275
Overs = 48.3

Expected Output:
Total Balls = 291
Run Rate = 5.67'''

runs,overs = map(float,input("Enter Total runs and Overs :").split())
x = overs*10
y = x%10/6
z = x//10 
total_balls =(y+z)*6 
run_rate = runs/(total_balls/6)
print("Total Balls :",total_balls,"\nRun Rate:",run_rate)

