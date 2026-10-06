'''1. Utility Toolkit System

You are developing a Utility Toolkit Application for a small office. Employees use this tool to quickly perform common number operations like checking prime numbers, reversing numbers, etc.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Check Prime Number
2 → Check Palindrome Number
3 → Reverse a Number
4 → Count Digits
5 → Exit

Sample Run 1:
Input:
Enter your choice: 1
Enter number: 7

Output:
7 is a Prime Number

Sample Run 2:
Input:
Enter your choice: 2
Enter number: 121

Output:
121 is a Palindrome Number

Sample Run 3:
Input:
Enter your choice: 3
Enter number: 456

Output:
Reversed Number is: 654

Sample Run 4:
Input:
Enter your choice: 4
Enter number: 98765

Output:
Total digits: 5

Sample Run 5 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

Sample Run 6 (Exit):
Input:
Enter your choice: 5

Output:
Exiting program... Thank you!

Requirements:

* Use while loop to repeat menu
* Use match-case for decision making
* Handle negative numbers properly
* Use only loops and conditions'''


while True:
    print("\nMenu Options:\n1 → Check Prime Number\n2 → Check Palindrome Number\n3 → Reverse a Number\n4 → Count Digits\n5 → Exit")
    choice = int(input("Enter Choice = "))
    match choice:
        case 1:
            num = int(input("Enter Number  = "))
            i = 2
            org = num
            if num<2:
                print(org,"is not Prime Number ")
            else:
                while i<=num//2:
                    if num%i==0:
                        print(org,"is not Prime Number")
                        break
                    i+=1
                else:
                    print(org," is Prime Number")
        case 2:
            num = int(input("Enter Number = "))
            org = num
            rev=""
            for i in str(num):
                rev=i+rev
            if int(rev)==num:
                print(org,"is Polindrome Number")
            else:
                print(org,"is not Polindrome Number")
        case 3:
            rev=""
            num = input("Enter Number = ")
            for i in num:
                rev=i+rev
            print("Reverse Number is :",rev)

        case 4:
            count=0
            num = input("Enter Number = ")
            for i in num:
                count+=1
            print("Total Digits =",count)
        case 5:
            print("Exiting program... Thank you!")
            break           
        case _:
            print("Invalid choice. Please try again.") 