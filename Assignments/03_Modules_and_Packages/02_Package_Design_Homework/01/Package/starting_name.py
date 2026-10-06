def vovel_starting(x):
    x = x.split()
    s1 = ("aeiouAEIOU")
    count=0
    for i in x:
        if i[0] in s1:
            count+=1
    return count