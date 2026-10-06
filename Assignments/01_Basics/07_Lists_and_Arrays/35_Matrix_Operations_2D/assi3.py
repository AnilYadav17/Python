'''3.=========================================================
         MATRIX QUALITY CHECK SYSTEM
=========================================================

Scenario

A manufacturing company records quality inspection values in
matrix form. The Quality Control team wants a menu-driven
application to analyze the inspection data and generate reports.

The application should allow the user to:

1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Count Armstrong Numbers Row-wise
   2. Count Palindrome Numbers Column-wise
   3. Display Average of Each Row
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Count Armstrong Numbers Row-wise
   -------------------------------------------
   Count and display the number of Armstrong numbers
   present in each row.

   Examples:
   153, 370, 371, 407

5. Choice 2 - Count Palindrome Numbers Column-wise
   -----------------------------------------------
   Count and display the number of palindrome numbers
   present in each column.

   Examples:
   121, 131, 444, 1221

6. Choice 3 - Display Average of Each Row
   --------------------------------------
   Calculate and display the average of each row.

7. Choice 4 - Exit
   --------------------------------------
   Display:
   "Thank You for Using Matrix Quality Check System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit

Enter your choice: 1

Enter rows: 3
Enter columns: 3

Enter matrix elements:
153 121 10
370 22 44
407 15 131

Output:
Row 1 Armstrong Count = 1
Row 2 Armstrong Count = 1
Row 3 Armstrong Count = 1

---------------------------------------------------------

Enter your choice: 2

Output:
Column 1 Palindrome Count = 0
Column 2 Palindrome Count = 3
Column 3 Palindrome Count = 2

========================================================='''
while True:
    print("""\n=========================================================
         MATRIX QUALITY CHECK SYSTEM
=========================================================
1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit""")
    
    choice = int(input("Enter your choice: "))
    match (choice):
        case 1:
            rows = int(input("Enter number of Rows: "))
            cols = int(input("Enter number of columns: "))

            matrix1 = []
            for i in range(rows):
                row = []
                for j in range(cols):
                    row.append(int(input(f"{j+1} Element: ")))
                matrix1.append(row)

            for i in range(len(matrix1)):
                count = 0  
                for j in range(len(matrix1[i])):
                    v = matrix1[i][j]
                    power = len(str(matrix1[i][j]))
                    digit_sum = 0
                    while v > 0:
                        digit = v % 10
                        digit_sum += digit ** power
                        v = v // 10
                    if digit_sum == matrix1[i][j]:
                        count += 1
                print(f"Row {i+1} Armstrong Count = {count}")
            
        case 2:
            rows = int(input("Enter number of Rows: "))
            cols = int(input("Enter number of columns: "))

            matrix1 = []
            for i in range(rows):
                row = []
                for j in range(cols):
                    row.append(int(input(f"{j+1} Element: ")))
                matrix1.append(row)

            print("\nMatrix1: ")
            for i in matrix1:
                for j in i:
                    print(j, end=" ")
                print()

            for i in range(len(matrix1[0])):
                count = 0
                for j in range(len(matrix1)):
                    val = matrix1[j][i]
                    is_palindrome = True
                    if str(val) != str(val)[::-1]:
                        is_palindrome = False
                    if is_palindrome:
                        count += 1
                print(f"Column {i+1} Palindrome Count = {count}")

        case 3:
            rows = int(input("Enter number of Rows: "))
            cols = int(input("Enter number of columns: "))

            matrix1 = []
            for i in range(rows):
                row = []
                for j in range(cols):
                    row.append(int(input(f"{j+1} Element: ")))
                matrix1.append(row)

            print("\nMatrix: ")
            for i in matrix1:
                for j in i:
                    print(j, end=" ")
                print()
            k = 0    
            for i in matrix1:
                d_sum = 0
                for j in i:
                    d_sum += j
                print(f"Row {k+1} Average = {d_sum/len(i)}")
                k += 1

        case 4:
            print("Thank You for Using Matrix Quality Check System")
            break