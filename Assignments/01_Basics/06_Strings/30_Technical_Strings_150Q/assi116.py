'''116. Check if a string is a valid shuffle of two other strings.'''
# S1 = "xy", S2 = "12", S3 = "x1y2" -> TRUE
s1 = input("Enter String 1: ")
s2 = input("Enter String 2: ")
s3 = input("Enter Shuffle String (String 3): ")

if len(s1) + len(s2) != len(s3):
    print("FALSE")
else:
    i, j, k = 0, 0, 0
    valid = True
    while k < len(s3):
        if i < len(s1) and s3[k] == s1[i]:
            i += 1
        elif j < len(s2) and s3[k] == s2[j]:
            j += 1
        else:
            valid = False
            break
        k += 1
    
    if valid and i == len(s1) and j == len(s2):
        print("TRUE")
    else:
        print("FALSE")
