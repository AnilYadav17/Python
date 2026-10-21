'''2. Reverse Sentence + Reverse Each Word

Secret Military Communication Decoder
A defense organization stores highly confidential messages in encrypted form.
To decode the message:

1. Reverse the entire sentence.
2. Reverse every individual word.
3. Store the final result back into the original string variable.

You must use the split() method.
Input:

```
Python is powerful
```

Output:

```
lufrewop si nohtyP'''

s1 = input("Enter String: ")
lst1 = s1.split()
result=""

for i in range(len(lst1)-1,-1,-1):
    words = lst1[i]
    for j in range(len(words)-1,-1,-1):
        result+=words[j]
    result+=" "
s1=result
print("Result: ",s1)
