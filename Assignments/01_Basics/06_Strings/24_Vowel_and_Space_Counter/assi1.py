'''1.Vowel Counter in Customer Feedback

 A company wants to analyze customer feedback messages by counting how many vowels are present in the feedback.

Input: Enter feedback message: Hello Customer Service

Output: Total vowels: 8
'''

str1 = input("Enter feedback message: ").lower()
count=0
for i in str1:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        count+=1
    
print("Total vowels:",count)