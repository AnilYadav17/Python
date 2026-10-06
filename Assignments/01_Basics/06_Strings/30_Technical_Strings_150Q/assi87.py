'''87. Print all permutations of a string with repetition.'''

s = input("Enter string: ")
used = []

for i in range(len(s)):
    for j in range(len(s)):
        for k in range(len(s)):

            if i != j and j != k and i != k:

                perm = s[i] + s[j] + s[k]

                if perm not in used:
                    used.append(perm)
                    print(perm)