#1. 
'''s = "Python"
print(s[0])
->  P '''

#2.
'''s = "Hello"
print(len(s))
-> 5 '''

#3
'''for i in range(2):
	for j in range(2):
		print("*", end="")
-> (B) **** '''

#4
'''s = "Programming"
print(s[-1])
-> B) g'''

#5
'''s = "Python"
print(s[1:4])
b) yth'''

#6
'''for i in range(3):
	for j in range(i):
		print(j, end="")
-> 001 '''

#7
'''s = "abcdef"
print(s[::2])
-> ace  '''

#8
'''for i in range(3):
	for j in range(2):
		print("Hi")
-> 6 times "Hi"'''

#9
'''s = "Python"
print(s[::-1])
A) nohtyP '''

#10
'''s = "Computer"
print(s[2:-2])
-> A) mput'''


#11
'''for i in range(2):
	for j in range(3):
		print(i+j, end=" ")
->   A) 0 1 2 1 2 3'''


#12
'''s = "Python"
print(s[10:])
-> C) "" (empty string)'''

#13
'''s = "abcdef"
print(s[-4:-1])
-> B) cde'''

#14
'''s = "DataScience"
print(s[4:])
-> B) Science'''

#15
'''count = 0
for i in range(4):
	for j in range(4):
		count += 1
print(count)
-> C) 16'''

#16
'''s = "PYTHON"
print(s[-1:-5:-1])
-> A) NOHT'''

#17
'''for i in range(1,4):
	for j in range(i,4):
		print("*", end="")
	print()
-> A)
***
**
*'''

#18
'''s = "abcdefghij"
print(s[8:2:-2])
-> ige'''

#19
'''s = "Python"
for i in range(len(s)):
	print(s[:i], end="|")
-> A)
|P|Py|Pyt|Pyth|Pytho|'''


#20
'''s = "ABCDE"
for i in range(len(s)):
	for j in range(i, len(s)):
		print(s[j], end="")
	print()
-> A)
ABCDE
BCDE
CDE
DE
E'''
