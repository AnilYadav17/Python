def print_down(x):
    print(x)
    if x<=1:
        return 1
    else:
        print_down(x-1)
    
    

print(print_down(5))