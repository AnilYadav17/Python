'''2.
Space Counter in Chat Messages

A chat application wants to calculate how many spaces are used in a message.

Input: Enter chat message: Good morning everyone how are you

Output: Total spaces: 5'''

str = input("Enter chat message: ")

#using method
#print("Total spaces:",str.count(" "))

#manualy
count=0
for ch in str:
    if ch==" ":
        count+=1
print("Total spaces:",count)