'''5.
 Student Grade Classification System (Python List Assignment)


A school stores student marks in a list. The system must analyze the marks and generate a **clear performance report** 
by grouping students into grade categories.



Write a Python program to:

* Iterate through the list of marks
* Assign grades based on marks:

  * **>= 90 → A**
  * **>= 75 and < 90 → B**
  * **>= 50 and < 75 → C**
  * **< 50 → Fail**
* Store each category in separate lists
* Count students in each category
* Display a **final structured report (important)**

---

## 📌 Output Format (Mandatory)

Your output must be displayed exactly in this format:

```
===== STUDENT GRADE REPORT =====

A Grade Students   : [list]
B Grade Students   : [list]
C Grade Students   : [list]
Fail Students      : [list]

--------------------------------
A Count   : X
B Count   : X
C Count   : X
Fail Count: X
--------------------------------

Total Students: X
```

---

 Input

[95, 82, 67, 45, 30]

Output

```
===== STUDENT GRADE REPORT =====

A Grade Students   : [95]
B Grade Students   : [82]
C Grade Students   : [67]
Fail Students      : [45, 30]

--------------------------------
A Count   : 1
B Count   : 1
C Count   : 1
Fail Count: 2
--------------------------------
Total Students: 5'''

#length and elements from user
n = int(input("Enter number of Students: "))
arr=[]
for i in range(n):
    x = int(input(f"Mark{i+1}: "))
    arr.append(x)

A_grade=[]
B_grade=[]
C_grade=[]
fails=[]

for i in arr:
    if i>=90:
        A_grade.append(i)
    elif i>=75:
        B_grade.append(i)
    elif i>=50:
        C_grade.append(i)
    else:
        fails.append(i)



print(f"""===== STUDENT GRADE REPORT =====

A Grade Students   : {A_grade}
B Grade Students   : {B_grade}
C Grade Students   : {C_grade}
Fail Students      : {fails}

--------------------------------
A Count   : {len(A_grade)}
B Count   : {len(B_grade)}
C Count   : {len(C_grade)}
Fail Count: {len(fails)}
--------------------------------
Total Students: {n}""")
