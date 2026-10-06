def sum(x):
    if x==1:
        return 1
    else:
        return x + sum(x - 1)
    

print(sum(10))