'''83.Create a string from a byte array.'''
ch=[72,101,108]
result=""

for i in range(len(ch)):
    result+=chr(ch[i])
print(result)