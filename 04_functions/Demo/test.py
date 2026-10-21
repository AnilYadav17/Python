'''
def greet(x):
    print("Hello",x)
greet("Anill")       #-> Returns value only

print(greet("Anil"))  #-> Returns None also
'''



'''
Assign values
def f(a,b,c):
    return [a+b+c,a-b-c,a*b*c]   #-> By default set ,but can be list,set,dict also

x = f     #-> Assigning func to another refference 
print(x(1,2,3))
'''

'''
Nested Function
def greet(x):
    return f"hello {x}"

def ex(x):
    print(x)

ex(greet("Anil"))'''


#LEGB  -> Local Enclosing Global BuiltIn

'''
VARIABLE SHADOWING 
x = 100
def func():
    x=5
    print(x)     #->5
func()
print(x)         #->100
In this not global variable can be changed
'''

'''
x = 100
def func():
    global x
    x=5
    print(x)     #->5
func()
print(x)         #-> 5
It will update the global variable
'''


'''16. What Are Positional Arguments?

Arguments assigned according to position.

def introduce(name, age):
    print(name, age)

introduce("Anil", 21)

Output:

Anil 21

Mapping:

name = "Anil"
age  = 21

Position matters.

Wrong order:

introduce(21, "Anil")

Output:

21 Anil

Python doesn't know your intention.

17. What Are Keyword Arguments?

Arguments assigned by parameter name.

def introduce(name, age):
    print(name, age)

introduce(age=21, name="Anil")

Output:

Anil 21

Order doesn't matter.

Benefits:

create_user(
    username="anil",
    age=21,
    city="Indore"
)

More readable.

18. What Are Default Arguments?

Parameters with default values.

def greet(name="Guest"):
    print(name)

Call:

greet()

Output:

Guest

Override default:

greet("Anil")

Output:

Anil

Real-world:

def connect(host="localhost", port=3306):
    pass
19. What Are Variable-Length Arguments?

Sometimes you don't know how many arguments will come.

Example:

add(1,2)
add(1,2,3)
add(1,2,3,4,5)

Normal parameters can't handle this.

Use *args.'''

'''def outer():
    numbers=[]

    def inner(x):
        x = input()
        numbers.append(x)
        print(numbers)

    return inner

y = outer()
y(1)'''


'''
#Decorators 
def dec(org_fun):
    def wrapper():
        print("Before run")
        org_fun()
        print("After run")
    return wrapper

@dec
def display():
    print("Hiii")


display()'''

def dec(org_fun):
    def wrapper():
        print("Before run")
        org_fun()
        print("After run")
    return wrapper

def display():
    print("Hiii")
    

def add(a,b):
    return a+b

x = dec(display)
x()

y = dec(add(1,2))
y()