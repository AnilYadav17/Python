try:
    x = int(input("Enter Value: "))
    print(10/x)

except Exception:
    print("Parent : Issue is there")

except ValueError:
    print("Child : Give integer value")

'''except ValueError:
    print("Child : Give integer value")
except Exception:
    print("Parent : Issue is there")'''


print("-"*100)

try:
    x = int(input("Enter Value: "))
    print(10/x)
    print("hii"+5)

except (ValueError,TypeError):
    print("Type or Value Error ")