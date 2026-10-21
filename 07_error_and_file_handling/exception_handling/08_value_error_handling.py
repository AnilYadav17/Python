try:
    x = int(input("Enter Value: "))
    print(10/x)

except ValueError as v:
    print("Value Error\n",v)


except Exception as e:
    print("Error\n",e)

else:
    print("Try Block runs without any error")


finally:
    print("Always Execute")