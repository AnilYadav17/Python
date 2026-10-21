'''62. Count vowels and consonants.'''

s = input("Enter string (only alphabets allowed):")
vowels = "aeiouAEIOU"
v_count=0
c_count=0

for i in s:
    if i in vowels:
        v_count+=1
    else:
        c_count+=1

print("Vowels:{} ,Consonents:{}".format(v_count,c_count))