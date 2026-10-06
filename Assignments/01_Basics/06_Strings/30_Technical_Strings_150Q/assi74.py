'''74 .Find the longest substring without repeating characters..'''
#S = "abcabcbb" -> abc
s = input("Enter string: ")
result=""

max=0

for i in range(len(s)):
    for j in range(i,len(s)):
        sub = s[i:j+1]

        unique=True
        for k in sub:
            count=0
            for l in sub:
                if k==l:
                    count+=1
            if count>1:
                unique=False
                break

        if unique and len(sub)>max:
            max=len(sub)
            result=sub            

print(f"Longest substring with non-rep character: {result} ")