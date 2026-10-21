#1. What is the output of [x for x in range(6) if x % 2 != 0]? -> A) [1, 3, 5]

#2. Which expression doubles even numbers and keeps odd numbers as-is? -> B) [x * 2 if x % 2 == 0 else x for x in my_list]

#3. How do you create a 3x2 matrix (3 rows, 2 columns) filled with zeros? -> C) [[0 for _ in range(2)] for _ in range(3)]

#4. Given matrix = [[1, 2], [3, 4]], which flattens it into [1, 2, 3, 4]? -> B) [val for row in matrix for val in row]

#5. True or False: A list comprehension modifies the original list in-place. -> B) False

#6. How do you filter for numbers that are both greater than 10 AND even? -> A) [x for x in nums if x > 10 if x % 2 == 0]

#7. Which structure correctly adds 1 to every integer in a 3D list cube? -> B) [[[v + 1 for v in row] for row in block] for block in cube]

#8. If matrix = [[10, 20], [30, 40]], how do you access the value 30? -> B) matrix[1][0]

#9. What is the result of [i*j for i in [1, 2] for j in [10, 20]]? -> A) [10, 20, 20, 40]

#10. True or False: Use a list comprehension to update a single value at matrix[0][0]. -> B) False

#11. Which correctly transposes a 2x3 matrix into a 3x2 matrix? -> A) [[row[i] for row in matrix] for i in range(len(matrix[0]))]

#12. Given data = [[[1], [2]], [[3], [4]]], what index path reaches the value 3? -> B) data[1][0][0]

#13. Which expression converts ['apple', 'be', 'cherry'] to ['APPLE', 'be', 'CHERRY']? -> B) [s.upper() if len(s) > 2 else s for s in words]

#14. How do you keep ONLY positive numbers within nested sublists [[1, -1], [2, -2]]? -> B) [[x for x in g if x > 0] for g in groups]

#15. What is the risk of using grid = [[0]*3]*3 to initialize a 2D list? -> B) Updating grid[0][0] will update the first element of every row due to shared references.

#16. To save memory with a large range (e.g., 10 million), what should you use instead of []? -> B) (x for x in range(10000000))

#17. What is the output of [name[:3] for name in ['Python', 'Ruby']]? -> A) ['Pyt', 'Rub']

#18. Which result is produced by [[i for i in range(j)] for j in range(3)]? -> B) [[], [0], [0, 1]]

#19. How do you find the intersection of two lists list1 and list2? -> A) [x for x in list1 if x in list2]

#20. Why are list comprehensions often preferred over standard for loops? -> B) They are more readable for simple transformations and optimized internally.
