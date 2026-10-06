'''
=========================================
MOBILE APP DOWNLOAD COUNTER
===========================

Downloads received from different cities:

cities = ["Indore","Bhopal","Indore","Pune","Delhi","Pune","Indore"]

Write a program to:

* Count downloads city-wise.
* Display city with maximum downloads.

Sample Output:
{'Indore':3,'Bhopal':1,'Pune':2,'Delhi':1}
Most Downloads : Indore
'''

cities = ["Indore", "Bhopal", "Indore", "Pune", "Delhi", "Pune", "Indore"]
downloads = {}

for city in cities:
    downloads[city] = downloads.get(city, 0) + 1

print(downloads)

# Find city with maximum downloads
max_city = None
max_downloads = 0

for city, count in downloads.items():
    if count > max_downloads:
        max_downloads = count
        max_city = city

print("Most Downloads :", max_city)
