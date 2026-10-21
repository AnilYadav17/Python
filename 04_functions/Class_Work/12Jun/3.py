#Dynamic -> Adding  two number .

a = int(input("Enter first: "))
b = int(input("ENter second: "))

def sum(x,y):               #here x,y are formal parameters
    print(f"Sum is {x+y}")       

sum(a,b)                    #here sum(a,b) is calling fuction and a,b are actual parameters