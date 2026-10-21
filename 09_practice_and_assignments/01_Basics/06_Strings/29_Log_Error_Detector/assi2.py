'''2. AI Auto-Correct Consecutive Word Remover

An AI-powered typing assistant often captures duplicate consecutive words while converting speech into text.

The company wants a Python program that removes only consecutive duplicate words while preserving the original sentence structure.

Input: hello hello hello team meeting meeting started

Output :hello team meeting started'''


s = input("Enter String: ")
l = s.split()
result=""


for i in l:
    if i not in result:
        result+=i+" "

print("Result:",result)
