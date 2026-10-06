'''3)	WAP to find out all the leap years between two entered years'''

y1 = int(input("Enter starting year = "))
y2 = int(input("Enter ending year = "))

while y1<=y2:
    if y1%100==0:
        if y1%400==0:
            print(y1)
    else:
        if y1%4==0:
            print(y1)
    y1+=1
