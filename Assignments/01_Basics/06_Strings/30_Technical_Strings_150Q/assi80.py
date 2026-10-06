'''80.Print list items containing all characters of a given word.'''

s1 = input("Enter string: ")
ch = input("Enter characters: ")

l1 = s1.split()
result=""

for i in l1:
    for j in i:
        if j in ch and j not in result:
            result+=j

print(result)