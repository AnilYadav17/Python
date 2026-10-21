from Packages.for_add import students
from Packages.for_total import total

def percentage():
    return total(students["marks"])/len(students["marks"])