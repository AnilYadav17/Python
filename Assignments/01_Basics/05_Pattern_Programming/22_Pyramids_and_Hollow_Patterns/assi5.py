'''5) Number-Star Palindrome
    12344321
    123**321
    12****21
    1******1'''

num = int(input("Enter Number: "))
i=num
while i>=1:
    print()
    #first
    j=1
    while j<=i:
        print(j,end="")
        j+=1
    
    #stars
    star=1
    while star<=(num-i)*2:
        print("*",end="")
        star+=1
    

    #second
    k=i
    while k>=1:
        print(k,end="")
        k-=1
    i-=1


