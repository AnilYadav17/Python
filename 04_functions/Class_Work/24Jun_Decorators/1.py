def mydecorator(x):
    def wrapper(*args,**krwargs):
        print("\nCalculation starting...")
        result = x(*args,**krwargs)
        print("Calculation done.\n")
        return result
    return wrapper

@mydecorator
def add(a,b):
    print("Sum is",a+b)


@mydecorator
def mul(a,b,c):
    print("Multi is:",a*b*c)



add(2,3)
mul(1,3,6)