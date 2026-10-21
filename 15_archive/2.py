num = int(input())

prev = num%10
num = num//10

differences=""

while num>0:
    digit = num%10
    diff = abs(prev-digit)
    differences = differences+" "+str(diff)
    prev = digit
    num= num//10

print(differences)