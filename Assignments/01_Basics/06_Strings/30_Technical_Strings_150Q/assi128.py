'''128. Check if a string follows a given pattern.'''
# Pattern = "abba", S = "dog cat cat dog" -> TRUE
pattern = input("Enter pattern (e.g., abba): ")
s_input = input("Enter string (e.g., dog cat cat dog): ")
words = s_input.split()

if len(pattern) != len(words):
    print("FALSE")
else:
    valid = True
    # Pairwise cross-validation checking
    for i in range(len(pattern)):
        for j in range(i + 1, len(pattern)):
            # If patterns match, words must match
            if pattern[i] == pattern[j] and words[i] != words[j]:
                valid = False
            # If patterns don't match, words must not match
            if pattern[i] != pattern[j] and words[i] == words[j]:
                valid = False
    
    if valid:
        print("TRUE")
    else:
        print("FALSE")
