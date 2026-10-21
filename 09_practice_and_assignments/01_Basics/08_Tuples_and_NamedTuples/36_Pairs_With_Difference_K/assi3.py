'''3.
MATRIX PERFORMANCE EVALUATION SYSTEM

A company records the monthly performance scores of employees in a matrix format. Each row represents an employee and each column represents a month.

The HR department wants a menu-driven application to analyze employee performance.

Menu
1. Find Employee with Highest Total Score
2. Find Month with Lowest Average Score
3. Display Employee-wise Maximum Score
4. Exit
Requirements
Choice 1 – Find Employee with Highest Total Score
Calculate the sum of each row.
Display the employee number having the highest total score.
Choice 2 – Find Month with Lowest Average Score
Calculate the average of each column.
Display the month having the lowest average score.
Choice 3 – Display Employee-wise Maximum Score
Find and display the maximum value present in each row.
Sample Input
10 20 30
40 50 60
25 35 45
Output
Employee 2 has Highest Total Score = 150

Month 1 Average = 25
Month 2 Average = 35
Month 3 Average = 45

Employee 1 Max Score = 30
Employee 2 Max Score = 60
Employee 3 Max Score = 45
'''


n = int(input("Enter number of Employees: "))
matrix=[]
for i in range(n):
    row=[]
    row = list(map(int,input(f"Enter Employee{i+1} per month score: ").split()))
    matrix.append(row)

while True:
    print("""
========= MATRIX PERFORMANCE EVALUATION SYSTEM ==
Menu
1. Find Employee with Highest Total Score
2. Find Month with Lowest Average Score
3. Display Employee-wise Maximum Score
4. Exit""")
    choice = int(input("Enter choice: "))
    match choice:
        case 1:
            highest = sum(matrix[0])
            highest_employee = 1

            for i in range(len(matrix)):
                r_sum = sum(matrix[i])

                if r_sum > highest:
                    highest = r_sum
                    highest_employee = i + 1

            print(f"Employee {highest_employee} has Highest Total Score = {highest}")

        case 2:
            months = len(matrix[0])

            lowest_avg = None
            lowest_month = None

            for j in range(months):
                col_sum = 0

                for i in range(len(matrix)):
                    col_sum += matrix[i][j]

                avg = col_sum / len(matrix)

                print(f"Month {j+1} Average = {avg}")

                if lowest_avg is None or avg < lowest_avg:
                    lowest_avg = avg
                    lowest_month = j + 1

            print(f"\nMonth {lowest_month} has Lowest Average Score = {lowest_avg}")

        case 3:
            print()

            for i in range(len(matrix)):
                print(f"Employee {i+1} Max Score = {max(matrix[i])}")

        case 4:
            print("Exiting Program...")
            break

        case _:
            print("Invalid Choice!")

            