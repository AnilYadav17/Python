try:
    d = {"a":1}
    x = input("Enter Key to access (only a available): ")
    print(d[x])

except KeyError:
    print("Please check key existence")