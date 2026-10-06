'''64.Count frequency of each vowel.'''

# s = input("Enter string:")
# vowels="aeiouAEIOU"
# result=""

# for i in s:
#     if i not in result:
#         count=0
#         if i in vowels:
#             count+=1
#         print(f"{i}:{count}"," ")
#         result+=i

s = input("Enter string: ")
vowels = "aeiouAEIOU"
result = ""

for i in s:
    if i not in result:
        if i in vowels:
            count = 0
            for j in s:
                if i == j:
                    count += 1
            print(f"{i}:{count}", end=" ")
        result += i