nums = [1,2,3,2,3,4]
k = int(input("Enter K: "))

unique = []
counts = []

for i in nums:
    if i not in unique:
        c = 0
        unique.append(i)
        for j in nums:
            if i == j:
                c += 1
        counts.append(c)

d = {}
for i, j in zip(unique, counts):
    d[i] = j

sorted_d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

keys = list(sorted_d.keys())

result = []
for i in range(k):
    result.append(keys[i])

print(result)
