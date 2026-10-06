'''4.  Instant Messaging Word Encryption System

A messaging application wants to temporarily encrypt messages during
transmission. The encryption rule is to reverse every word individually
while keeping the word positions unchanged.

Input: Enter message: java is powerful

Output: Encrypted Message: avaj si lufrewop'''

message = input("Enter message: ")
lst1 = message.split()
result=""
for i in range(len(lst1)):
    word = lst1[i]
    for j in range(len(word)-1,-1,-1):
        result=result+word[j]
    result+=" "
print("Encrypted Message:",result)