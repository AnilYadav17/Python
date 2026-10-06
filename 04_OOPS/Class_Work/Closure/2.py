def greet():
    x = "hii"

    def inner(y):
        nonlocal x
        return x+y
    return inner

g = greet()
print(g("Anil"))
print(g("Kannu"))
