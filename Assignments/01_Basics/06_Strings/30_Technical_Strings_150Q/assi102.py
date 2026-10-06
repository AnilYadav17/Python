'''102. Reverse a string using recursion.'''
# S = "abc" -> "cba"
def reverse_recursive(string):
    if len(string) <= 1:
        return string
    return string[-1] + reverse_recursive(string[:-1])

s = input("Enter string: ")
print("Reversed string =", reverse_recursive(s))
