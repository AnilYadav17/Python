'''49. Replace all consonants with '*' (Example suggests replacing non-vowels).'''
#Input: S = "apple"  , Output: "ap*le" (or similar output depending on implementation)


s = input("Enter string: ")
vowels = "aeiouAEIOU"
result=""


for i in s:
    if i in vowels:
        result+=i
    else:
        if i not in result:
            result+=i
        else:
            result+="*"

print(result)