'''8:
         SMART TEXT PROCESSING SYSTEM

A software company is developing a Smart Text Processing System for
handling user messages. Different users require different text
transformations. To avoid creating separate applications, the company
wants a menu-driven program where users can select operations according
to their requirements.

The system should continue executing until the user selects Exit.

====================================================== MENU
======================================================

===== Smart Text Processing System =====

1.  Reverse Complete String
2.  Reverse Every Word
3.  Reverse Word Order
4.  Exit

====================================================== Choice 1 :

Conditions: - Reverse the complete string - Ignore extra spaces - Keep
special characters (@,#,$,%) in their original positions - Do not use
built-in reverse functions

Example: Input: ja@va#py

Output: yp@av#aj

Test Case 1: ab@cd#ef Output: fe@dc#ba

Test Case 2: py@th#on Output: no@ht#yp

Test Case 3: java@proOutput : orpa@vaj

====================================================== Choice 2 :

Conditions: - Reverse every word separately - Words containing digits
should not be reversed - Ignore extra spaces between words - First
letter of each reversed word should become uppercase

Example: Input: java is easy123 programming

Output: Avaj Si easy123 Gnimmargorp

Test Case 1: python full stack22 developer Output: Nohtyp Lluf stack22
Repoleved

Test Case 2: hello java99 world Output: Olleh java99 Dlrow

====================================================== Choice 3 :

Conditions: - Reverse order of words - Remove duplicate words - Ignore
case while checking duplicates - Keep only first occurrence

Example: Input: Java python Java react Python

Output: React Python Java

Test Case 1: HTML CSS HTML Java CSS Output: Java CSS HTML

Test Case 2: Python React Java Python React Output: Java React Python

====================================================== Choice 4
======================================================

Program Closed Successfully'''


while True:
    print("""
===== Smart Text Processing System =====

1.  Reverse Complete String
2.  Reverse Every Word
3.  Reverse Word Order
4.  Exit
""")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            letters=""
            s1 = input("Enter String: ")
            for ch in s1:
                if ch.isalnum():
                    letters+=ch
            
            rev=""
            for i in range(len(letters)-1,-1,-1):
                rev+=letters[i]


            j=0
            for  i in range(len(s1)):
                if not s1[i].isalnum():
                    print(s1[i],end="")
                else:
                    print(rev[j],end="")
                    j+=1               
        
        case 2:
            s1 = input("Enter String: ").lower()
            lst1 = s1.split()
            result=""
            final=" "
            for i in range(len(lst1)):
                words =lst1[i]

                if words.isalpha():
                    for i in range(len(words)-1,-1,-1):
                        result+=words[i]
                    result+=" "
                else:
                    result+=words+" "
            for j in range(len(result)):
                if j==0 or result[j-1]==" ":
                    final+=chr(ord(result[j])-32)
                else:
                    final+=result[j]
            print("Result:",final)
        case 3:
            s1 = input("Enter String: ")

            lst1 = s1.split()

            unique = []

            # Remove duplicates (ignore case)
            for word in lst1:

                found = False

                for item in unique:
                    if word.lower() == item.lower():
                        found = True
                        break

                if not found:
                    unique.append(word)

            # Reverse word order manually
            result = ""

            for i in range(len(unique)-1, -1, -1):
                result += unique[i] + " "

            print("Output:", result)
        case 4:
            break

        case _:
            print("Please enter a valid choice")
