#WAP to merge two dictionaries and sum their values.

d1 = {"goa":5,"nepal":5, "delhi":8}
d2 = {"goa":2, "hyb":6, "delhi":8}
merged  = d1.copy()

for k,v in d2.items():
    merged[k]=merged.get(k,0)+v

print(merged)
