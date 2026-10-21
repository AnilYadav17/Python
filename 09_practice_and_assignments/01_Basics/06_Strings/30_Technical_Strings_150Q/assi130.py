'''130. Find the maximum occurring word.'''
# S = "a b a c a" -> 'a'
s = input("Enter string: ")
words = s.split()

max_word = ""
max_count = 0

for w in words:
    count = words.count(w)
    if count > max_count:
        max_count = count
        max_word = w

print("Maximum occurring word =", max_word)
