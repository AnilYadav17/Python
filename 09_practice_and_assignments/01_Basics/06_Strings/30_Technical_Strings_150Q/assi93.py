'''93 Match strings with wildcard characters ($\*$, ?).'''
#Pattern = "a?c", Text = "axcde"   -> TRUE



p = input("Enter pattern: ")
t = input("Enter text: ")

if len(p) > len(t):
    print("FALSE")
else:
    match = True

    for i in range(len(p)):
        if p[i] != '?' and p[i] != t[i]:
            match = False
            break

    print("TRUE" if match else "FALSE")