'''82.Create a string from a character array.'''
ch=['t','e','s','t']
result=""
for i in range(len(ch)):
    result+="".join(ch[i])
print(result)