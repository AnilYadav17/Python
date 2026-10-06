'''65.Count palindromic substrings.'''
# S = "aaa"  -> 6 (a, a, a, aa, aa, aaa)

#Remaining one :)
s = input("Enter string: ")
count=0


for i in range(len(s)):
    for j in range(i,len(s)):
        sub = s[i:j+1]
        if sub==sub[::-1]:
            count+=1

print(f"Count: {count}")