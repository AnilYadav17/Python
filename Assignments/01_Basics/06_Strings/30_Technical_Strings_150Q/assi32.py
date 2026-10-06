'''32.Count frequency of each word.'''

s = input("Enter string: ")
l = s.split()
result=" "

for i in l:

    if i not in result:
        count=0

        for j in l:
            if j==i:
                count+=1

        print(i,":",count)
        result+=i+" "