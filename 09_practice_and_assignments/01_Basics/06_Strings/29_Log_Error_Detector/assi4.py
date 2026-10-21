'''# 4. Cloud Storage Duplicate File Name Resolver

A cloud storage company stores uploaded filenames from users.

Sometimes multiple duplicate filenames are uploaded.

The system should:

* Keep the first occurrence unchanged
* Add (1), (2), (3)... for duplicates

Input: file file image file image data
Output: file file(1) image file(2) image(1) data '''

s1 = input("Enter FileNames: ").lower()

l1 = s1.split()

temp = ""
output = ""

for i in range(len(l1)):
    count = 0

    for j in range(i):

        if l1[i] == l1[j]:
            count += 1

    if count == 0:
        output += l1[i] + " "
    else:
        output += l1[i] + "(" + str(count) + ") "

print(output)