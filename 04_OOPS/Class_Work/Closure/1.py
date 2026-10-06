def outer():
    x = 0
    def inner():
        nonlocal x
        x+=1
        return x
    return inner

o  = outer()
print(o())
print(o())
print(o())
print(o())
print(o())
