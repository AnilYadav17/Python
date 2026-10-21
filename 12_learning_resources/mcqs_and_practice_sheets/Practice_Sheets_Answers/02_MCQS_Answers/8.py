#1. What will be the output?
'''t = (1,2,[3,4])
t[2].append(5)
print(t)
-> B) (1,2,[3,4,5])'''

#2. What is the output?
'''t=(10,20,30,40)
a,*b,c=t
print(a, b, c)
-> B) 10 [20,30] 40'''

#3. What is the type of t?
'''t=(1)
type(t)
-> C) int'''

#4. What is the type of t?
'''t=(1,)
type(t)
-> A) tuple'''

#5. What is the value of middle?
'''t=(1,2,3,4,5)
first,*middle,last=t
-> B) [2,3,4]'''

#6. What is the output of the slice?
'''nums=(1,2,3,4,5)
nums[::-2]
-> B) (5,3,1)'''

#7. Tuple packing means? -> C) Automatically create tuple from values

#8. What is the type of a?
'''a=10,20,30
type(a)
-> B) tuple'''

#9. What is the output?
'''(1,2)+(3,4)
-> A) (1,2,3,4)'''

#10. What is the value of t after appending?
'''t=([1,2],[3,4])
t[0].append(10)
-> ([1, 2, 10], [3, 4])'''

#11. What is the value of s.name?
'''Student=namedtuple("Student",["name","age"])
s=Student("Ram",20)
s.name
-> A) Ram'''

#12. What happens if you try p.x=50 in namedtuple? -> B) AttributeError

#13. What is the value of User.__name__?
'''User=namedtuple("Account",["id"])
User.__name__
-> B) Account'''

#14. Student._fields returns? -> B) tuple

#15. _replace() changes original? -> B) No creates new object

#16. namedtuple object indexing possible? -> A) Yes

#17. type(namedtuple object)? -> A) generated class

#18. Can namedtuple unpack? -> A) Yes

#19. Namedtuple is: -> B) immutable

#20. Namedtuple inherits behavior of: -> A) tuple
