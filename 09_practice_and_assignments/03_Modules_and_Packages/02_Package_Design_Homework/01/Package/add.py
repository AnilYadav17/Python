ages=[]
names=""

def add_details():
        global names
        global ages
        ages.extend(map(int,input("Enter ages using space: ").split()))
        names=input("Enter name using space: ")
        print("Details added successfully\n")