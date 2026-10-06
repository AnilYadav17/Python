'''4.
Consonant Counter in Student Name Record

A school management system wants to count how many consonants are present in student names.

Input: Enter student name: Ajay Singh Thakur

Output: Total consonants: 10

NOTE:

Ignore case sensitivity (treat A and a same)
Consider only English alphabets for vowel/consonant counting
Vowels: A, E, I, O, U'''

str1 = input("Enter student name: ").lower()
count=0
for i in str1:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i==" " or i>="0" and i<="9":
        pass
    else:
        count+=1
    
print("Total vowels:",count)