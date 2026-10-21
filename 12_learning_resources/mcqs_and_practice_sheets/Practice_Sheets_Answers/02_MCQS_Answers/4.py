#1. What is the primary purpose of string interning in Python? -> B) To optimize memory usage and speed up comparisons by reusing a single object for identical string literals.

#2. Which of the following code blocks will output True due to Python's implicit string interning?
'''a = "python_3"
b = "python_3"
print(a is b)
-> B)'''

#3. If you need to force Python to intern a dynamically generated string at runtime, which function should you use? -> B) sys.intern()

#4. Why does string interning require strings to be immutable? -> B) Because if a shared interned string were mutated, it would unexpectedly change the value of that string for all other variables referencing it.

#5. Consider the following code:
'''import sys
s1 = sys.intern("dynamic_string" + "123")
s2 = "dynamic_string123"
print(s1 is s2)
-> A) True'''

#6. Which statement is TRUE regarding the comparison of two long, identical interned strings? -> B) Python can compare their memory addresses using pointer equality, taking O(1) time.

#7. What happens if you try to run the following code?
'''language = "Python"
del language[0]
-> B) TypeError: 'str' object doesn't support item deletion'''

#8. How can you effectively delete the variable reference itself so that using it again causes a NameError? -> C) del text

#9. What is the idiomatic way to "delete" all occurrences of a specific character from a Python string? -> B) s.replace('a', '')

#10. Consider the code below:
'''msg = "B-a-n-a-n-a"
clean_msg = "".join(msg.split("-"))
-> B) Banana; the original msg remains completely unchanged in memory.'''

#11. You want to delete trailing characters from a string only if they match a specific suffix. Which method is cleanest in modern Python (3.9+)? -> B) s.removesuffix("suffix")

#12. What does the following expression evaluate to?
'''" hello ".strip()
-> C) "hello"'''

#13. What is the output of the following slice-based string manipulation?
'''word = "Indore"
print(word[1:5:2])
-> C) no'''

#14. What does the find() method return if the substring is NOT found? -> C) -1

#15. What is the output of this code snippet?
'''data = "apple,banana,cherry,dates"
print(data.split(",", 2))
-> A) ['apple', 'banana', 'cherry,dates']'''

#16. Which method will return True for the string "12³"? -> C) Both A and B

#17. How does the partition() method behave differently from split()? -> B) It always returns a 3-tuple containing: part before the separator, the separator itself, and the part after the separator.

#18. What is the output of the following code?
'''text = "python programming"
print(text.title())
-> C) Python Programming'''

#19. Consider the following code using zfill():
'''num = "-42"
print(num.zfill(5))
-> B) -0042'''

#20. What will be the output of the expression below?
'''"abc".center(7, "*")
-> B) **abc**'''
