'''Analyse the pattern and write code accordingly :
Input = 6
0
0 1
0 1 2
0 1 2 3
0 1 2 3 4'''


num = int(input("Enter Number = "))
i = 0
while i<num-1:
    print()
    j=0
    while j<=i:
        print(j,end="")
        j+=1
    i+=1
