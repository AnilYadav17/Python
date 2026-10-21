'''try:
    #Risky Code
except ExceptionType1:
    #hadle exception
except ExceptionType2:
    #hadle exception2
else:
    #Runs if no exception occurs
finally:
    #always execute'''



print("Welcome")
try:
    x = int("10")     #If x = int("abc") than Somehing went wrong
    print("Everything went well")
except :
    print("Something went wrong")
print("Rest of Code")


##The problem with above code is we do not know what error occurs.


try:
    print("try block Stated :---")
    y = int(input("For ZeroError:"))
    print(10/y)
    x = int(input("For ValueError:"))
    print("--: Try block ended ")

except ZeroDivisionError:
    print("Do not provide Zero")
except ValueError:
    print("Please Provide Intvalue.")