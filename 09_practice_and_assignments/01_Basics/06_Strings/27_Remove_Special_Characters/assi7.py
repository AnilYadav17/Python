'''7. 
Remove Duplicate Words from a String

Voice Assistant Noise Correction System

A voice assistant records spoken commands from users.

Due to microphone disturbance and network lag, some words are repeated multiple times.

The company wants a Python program that removes duplicate words while maintaining the original order.


Input: hello hello how are are you
Output: hello how are you'''



s1 = input("Enter Sentence:").lower()
l1 = s1.split()
result=""

for i in l1:
    count=0
    for j in result.split():
        if j==i:
            count+=1
    if count==0:
        result+=i+" "
print(result)