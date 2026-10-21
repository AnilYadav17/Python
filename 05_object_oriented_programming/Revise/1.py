class Student:
    
    def get_data(self):
        return f"Name: {self.name} \nRoll Number: {self.roll}\nCourse: {self.course}\n"
    
    def set_data(self,name,roll,course):
        self.name = name
        self.roll = roll
        self.course = course
        print("Name,Roll Number and Course are successfully updated!")

s1 = Student()
s2 = Student()

s1.set_data("Anil",1,'CSE')
s2.set_data("Abhi",2,'CSE')
print(s1.get_data())
print(s2.get_data())