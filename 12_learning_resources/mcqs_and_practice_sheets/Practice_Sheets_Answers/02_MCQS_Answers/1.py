#1. Python ternary operator -> B) true_value if condition else false_value
#2.output: 
'''x = 10
result = "Even" if x % 2 == 0 else "Odd"
print(result)
EVEN'''
#3. ? name -> A)Conditional Statement
#Q4. What keyword is used to start a structural pattern matching block in Python?   -> C) match
#Q5. Inside a match block, which keyword is used to define individual patterns to check against? -> B) case
#Q6. What is the purpose of the underscore (_) in a case _: statement?  -> B) It acts as a catch-all wildcard (default case) if nothing else matches.
#Q7:
'''color = "Red"
match color:
	case "Blue":
		print("Sky")
	case "Red":
		print("Fire")
FIRE will be output'''
#Q8. What keyword is used to add an extra condition (a guard) to a specific case?  -> c) if
#Q9. In the statement case x if x > 0:, what is the part if x > 0 called? ->  C) Guard condition
#Q10. 
'''age = 15
status = "Minor" if age < 18 else "Adult"
print(status)
B)Minor'''



#Q11. Which operator is used within a single case line to mean OR?   ->  | 
#Q12. 
'''grade = "B"
match grade:
	case "A" | "B":
		print("Good Job")
	case _:
		print("Try Harder")
Output will be A) Good Job'''
#Q13. In a ternary operator expression, when is the else value chosen?   ->   B) When the condition is False.
#Q14. What will happen if a match-case statement finds NO matching patterns and there is NO case _: included? -> B) The code simply moves on to the lines below the match block.
#15
'''num = 5
match num:
	case x if x % 2 == 0:
		print("Even Number")
	case x if x % 2 != 0:
		print("Odd Number")
Output will be Odd Number'''
#Q16. Does Python's match-case automatically fall through to execute the next case block after finding a successful match? -> B) No, it executes exactly one matching block and stops looking.
#
'''value = [10, 20]
match value:
	case [x, y]:
		print(x + y)
	case _:
		print("Not a pair")
C) 30'''
#Q18. A guard condition inside a case block is evaluated:   ->   B) Only after the structural pattern matches successfully.
#19.
'''is_logged_in = False
msg = "Welcome" if is_logged_in else "Please Login"
print(msg)

output will be B) Please Login'''
#20.
'''score = 45
match score:
	case s if s >= 50:
		print("Passed")
	case _:
		print("Failed")
Output will be B) Failed '''
