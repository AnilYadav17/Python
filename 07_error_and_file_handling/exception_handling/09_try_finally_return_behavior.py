def test():
    try:
        return "From TRY"
    finally:
        print("From FINALLY")
        #return "From FINALLY" -> only runs this is two returns are there 

print(test())


def test1():
    try:
        return 10/0
    except ZeroDivisionError:
        return "error handled"
    finally:
        print("From FINALLY")

    print("Demo")  #Here it will not work
