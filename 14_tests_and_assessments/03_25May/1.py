'''Find Occurrence of a Word in a String

Product Review Analysis System

An e-commerce company wants to analyze customer reviews.

The company wants a Python program to count how many times a particular word appe>

Input Sentence:

```
iphone is good and iphone battery is strong
```

Word:

```
iphone
```

Output: 2'''



s = input("Enter String:")
ch = input("Enter character:")
count=0

for i in range(len(s)-len(ch)+1):
	for j in range(len(ch)):
		if ch[j]!=s[i+j]:
			break
		else:
			count+=1

print(int(count/len(ch)))


