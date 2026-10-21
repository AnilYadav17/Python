s = input("Enter the String = ")
for ch in s:
    if ch in "aeiouAEIOU":
        continue
    print(ch,end="")