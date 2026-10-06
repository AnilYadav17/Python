'''126. Print all anagrams of a string.'''
# S = "cat" -> "cat, cta, act, atc, tca, tac"
def get_permutations(string):
    if len(string) <= 1:
        return [string]
    perms = []
    for i in range(len(string)):
        current = string[i]
        remaining = string[:i] + string[i+1:]
        for p in get_permutations(remaining):
            if current + p not in perms:
                perms.append(current + p)
    return perms

s = input("Enter string: ")
results = get_permutations(s)
print("Anagrams:", ", ".join(results))
