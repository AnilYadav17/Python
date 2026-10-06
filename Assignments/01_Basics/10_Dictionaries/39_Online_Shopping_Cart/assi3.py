'''=========================================
WEBSITE PAGE VISIT TRACKER
==========================

A website records page visits.

pages = ["Home","About","Home","Contact","Home","About"]

Write a program to:

* Count visits of each page using a dictionary.
* Display page name and visit count.

Sample Output:
Home visited 3 times
About visited 2 times
Contact visited 1 time'''

pages = ["Home","About","Home","Contact","Home","About"]
d = {}

for i in pages:
        d[i]=d.get(i,0)+1

for i,j in d.items():
        print(f"{i} visited {j} times")