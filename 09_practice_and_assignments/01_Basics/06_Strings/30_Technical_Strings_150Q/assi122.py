'''122. Convert a binary string to decimal.'''
# S = "101" -> 5
s = input("Enter binary string: ")
decimal = 0
valid = True

for char in s:
    if char != '0' and char != '1':
        valid = False
        break
    decimal = decimal * 2 + int(char)

if valid:
    print("Decimal value =", decimal)
else:
    print("Invalid binary string")
