'''3.
Character Occurrence Checker in Product Review

An e-commerce website wants to know how many times a particular character appears in a product review.

Input: Enter product review: this product is really good Enter character to check: o

Output: Character 'o' occurs: 3 times'''


str = input("Enter product review: ")
target = input("Enter character to check: ")

#using method
#x = str.count(target)
#print(f"Character 'o' occurs: {x} times")

#manualy
count=0
for ch in str:
    if ch==target:
        count+=1
print(f"Character 'o' occurs: {count} times")