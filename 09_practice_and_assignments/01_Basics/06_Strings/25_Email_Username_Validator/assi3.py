'''3.
Word Counter in Complaint Message

A customer care system wants to count how many words are present in a complaint message.

Input:
Enter complaint: Delivery was delayed again today

Output:
Total words: 5'''

# without method
complaint = input("Enter complaint: ")
count = 0

for ch in range(len(complaint)):

    if complaint[ch] != " " and (ch == 0 or complaint[ch - 1] == " "):
        count += 1

print("Total words:", count)

# #with method
# complaint = input("Enter complaint: ")
# lst1 = complaint.split()
# print(len(lst1))
