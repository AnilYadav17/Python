from Package import add,second_high,senoirs,remove_duplicates,starting_name,longest_empname

add.add_details()
ages = add.ages
names = add.names

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
            print("Second Highest Age :",second_high.s_highest(ages))
        case 2:
            print("Senior Employees :",senoirs.senior_emp(ages))
        case 3:
            print("Unique Ages :",remove_duplicates.remove_dup(ages))
        case 4:
            print("Names Starting with Vowel :",starting_name.vovel_starting(names))
        case 5:
            print("Longest Employee Name :",longest_empname.longest_emp_name(names))
        case 6:
            print("Thanks for visiting...")
            break
        case _:
            print("Invalid choice")