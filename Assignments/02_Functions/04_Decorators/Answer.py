ages=[]
names=""

def add_details():
        global names
        global ages
        ages.extend(map(int,input("Enter ages using space: ").split()))
        names=input("Enter name using space: ")
        print("Details added successfully\n")


def s_highest(x):
    highest = second = float('-inf')
    for i in x:
        if i > highest:
            second = highest
            highest = i
        elif highest > i > second:
            second = i
    return second
     
def senior_emp(x):
    count=0
    for i in x:
        if i>50:
            count+=1
    return count

def remove_dup(x):
    return sorted(list(set(x)))

def vovel_starting(x):
    x = x.split()
    s1 = ("aeiouAEIOU")
    count=0
    for i in x:
        if i[0] in s1:
            count+=1
    return count

def longest_emp_name(x):
    x = x.split()
    l_name_emp = x[0]
    for i in x:
        if len(i)>len(l_name_emp):
            l_name_emp = i
    return l_name_emp

add_details()
while True:
    print("""
========== EMPLOYEE DATA PROCESSING SYSTEM ==========
1. Find Second Highest Employee Age
2. Count Senior Employees
3. Remove Duplicate Ages
4. Count Names Starting with a Vowel
5. Find Longest Employee Name
6. Exit
====================================================
""")
   
    choice = int(input("Enter choice: "))
    match choice:
        case 1:
            print("Second Highest Age :",s_highest(ages))
        case 2:
            print("Senior Employees :",senior_emp(ages))
        case 3:
            print("Unique Ages :",remove_dup(ages))
        case 4:
            print("Names Starting with Vowel :",vovel_starting(names))
        case 5:
            print("Longest Employee Name :",longest_emp_name(names))
        case 6:
            print("Thanks for visiting...")
            break
