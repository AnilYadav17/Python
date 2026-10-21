#1. Given the list nums = [10, 20, 30, 40, 50, 60], what will nums[1:4] return? -> B) [20, 30, 40]

#2. Which of the following expressions correctly reverses a list lst using slicing? -> C) lst[::-1]

#3. What is the output of the following Python code snippet?
'''letters = ['a', 'b', 'c', 'd', 'e']
print(letters[2:])
-> B) ['c', 'd', 'e']'''

#4. What will be the output of the following slice operation?
'''data = [1, 2, 3, 4, 5, 6, 7, 8]
print(data[1:7:2])
-> A) [2, 4, 6]'''

#5. Consider the statement: mystr = [5, 10, 15, 20]. What does mystr[:-1] yield? -> B) [5, 10, 15]

#6. If you execute my_list.remove(x), what happens if the value x appears multiple times in my_list? -> C) Only the first occurrence of x is removed.

#7. What happens if you call .remove(100) on a list that does not contain the element 100? -> C) It raises a ValueError.

#8. Which list method removes and returns the last element of a list by default? -> C) pop()

#9. What will be the output of the following code snippet?
'''fruits = ['apple', 'banana', 'cherry']
result = fruits.pop(1)
print(fruits, result)
-> A) ['apple', 'cherry'] banana'''

#10. How do you completely delete all items from a list named items, leaving it completely empty? -> B) items.clear()

#11. What is the main difference between the del statement and the .remove() method? -> A) del deletes by index, whereas remove() deletes by value.

#12. What is the output of the following code?
'''arr = [10, 20, 30, 40]
del arr[1:3]
print(arr)
-> A) [10, 40]'''

#13. Which list method adds an item to the end of the list? -> C) append()

#14. What will be the final state of list x after running this code?
'''x = [1, 2]
x.extend([3, 4])
print(x)
-> B) [1, 2, 3, 4]'''

#15. What does items.insert(0, 'A') do on a non-empty list items? -> B) Adds 'A' at the very beginning of the list, shifting existing items to the right.

#16. What will be the output of the following sequence?
'''vowels = ['e', 'a', 'u', 'o', 'i']
vowels.sort()
print(vowels)
-> C) ['a', 'e', 'i', 'o', 'u']'''

#17. How does the list method .sort() differ from the built-in function sorted()? -> A) sort() modifies the original list in-place; sorted() returns a new sorted list.

#18. What is the output of the following code block?
'''numbers = [1, 2, 3, 2, 4, 2]
print(numbers.count(2))
-> C) 3'''

#19. If values = [10, 20, 30, 40], what is returned by values.index(30)? -> A) 2

#20. What is the slice outcome of my_list[5:2] if my_list contains 10 items? -> B) An empty list []
