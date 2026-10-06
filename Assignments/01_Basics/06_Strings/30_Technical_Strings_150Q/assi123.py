'''123. Convert a decimal number to binary string.'''
# N = 5 -> "101"
n = int(input("Enter decimal number: "))

if n == 0:
    binary = "0"
else:
    binary = ""
    temp = n
    while temp > 0:
        binary = str(temp % 2) + binary
        temp = temp // 2

print("Binary string =", binary)
