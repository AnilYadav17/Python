words =["fl","fleek","fleep","fleeeer"]

first_word = words[0]
result=""

for i in range(len(first_word)):
    match=True
    for word in words:
        if i >= len(word) or word[i] != first_word[i]:
                match=False
                break
    if match:
         result+=first_word[i]
    else:
         break        

print(result)