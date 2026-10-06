'''59.Rotate characters right by 3 positions.'''
s = input("Input string: ")
result=""

result+=s[-3:]

for i in range(len(s)-3):
    result+=s[i]


print("Result:",result)