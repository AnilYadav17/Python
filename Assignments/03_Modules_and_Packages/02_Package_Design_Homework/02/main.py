from Packages import for_add,for_total,for_per,for_grade,for_max,for_min,for_result


students = for_add.students
add_details = for_add.add_details
total = for_total.total
percentage = for_per.percentage
grade = for_grade.grade
result= for_result.result
maximum = for_max.maximum
minimum = for_min.minimum


while True:
	print("""
================================
STUDENT RESULT MANAGEMENT SYSTEM
================================
MENU
1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Complete Result
6. Find Highest Subject Mark
7. Find Lowest Subject Mark
8. Exit
""")
	choice = int(input("Enter Choice: "))
	match choice:
		case 1:
			name = input("Enter Student Name : ")
			roll = int(input("Enter Roll Number : "))
			n = int(input("Enter number of Subjects: "))
			marks=[]
			for i in range(n):
				marks.append(int(input(f"Enter Mark {i+1} :")))
			
			add_details(name,roll,*marks)

		case 2:
		    print(f"Total Marks : {total(students['marks'])}")

		case 3:
		    print(f"Total Percentage : {percentage()}")
		    
		case 4:
		    print(f"Grade : {grade(percentage())}")
		    
		case 5:
		    result()
		    
		case 6:
		    print(f"Highest Mark: {maximum(students['marks'])}")
		
		case 7:
		    print(f"Lowest Mark : {minimum(students['marks'])}")
		    
		case 8:
		    print("Thank You. Program Terminated.")
		    break
		    
		case _:
			print("Enter a valid choice!")
