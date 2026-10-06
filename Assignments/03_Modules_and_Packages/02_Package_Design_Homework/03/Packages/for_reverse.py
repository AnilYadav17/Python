def reverse(n):
    rev = ""
    while n>0:
        d=n%10
        rev+=str(d)
        n=n//10
    return rev
