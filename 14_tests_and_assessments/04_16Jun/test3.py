'''
3. 3.5 marks

Secure Password Analysis

A cybersecurity team wants to identify pairs of passwords having no common characters.

Problem Statement:

Given N strings, count the number of pairs that do not share any common character.

Example:

Input

N = 4
passwords[] = {"abc", "de", "fg", "ad"}

Output

3

Explanation

("abc","de") 
("abc","fg")
("de","fg")
'''


n = int(input("Enter number of Words: "))
passwords = list(input("Enter words using spaces: ").split())
count = 0

for i in range(len(passwords)):
    for j in range(i + 1, len(passwords)):
        common = False
        for char in passwords[i]:
            if char in passwords[j]:
                common = True
                break
        if not common:
            count+= 1

print(count)
