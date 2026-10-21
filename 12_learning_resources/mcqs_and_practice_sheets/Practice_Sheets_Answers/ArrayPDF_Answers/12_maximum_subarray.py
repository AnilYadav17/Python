a = [5,4,-1,7,8]
high=0
for i in range(len(a)):
        for j in range(i,len(a)):
                sum=0
                sub=a[i:j+1]
                for k in sub:
                        sum+=k
                if high<sum:
                        high=sum

print(high)
