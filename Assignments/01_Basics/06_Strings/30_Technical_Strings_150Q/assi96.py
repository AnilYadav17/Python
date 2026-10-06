'''96. Find the second most frequent word.'''
# S = "a b a c b", -> 'c'
s = input("Enter string: ")
words = s.split()

first = 0
second = 0

for w in words:
    count = words.count(w)
    if count > first:
        second = first
        first = count
    elif count > second and count != first:
        second = count

found = False
for w in words:
    if words.count(w) == second:
        print("Second Most Frequent Word =", w)
        found = True
        break

if not found:
    print("No second most frequent word found")
