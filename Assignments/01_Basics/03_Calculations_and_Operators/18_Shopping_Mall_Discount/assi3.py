'''3. Employee Bonus Distribution System
A company provides bonuses based on years of experience.
Experience >10 years → 30% bonus
Experience >5 years → 20% bonus
Otherwise → 10% bonus'''

experience = int(input("Enter Years of Experience = "))

print("30% Bonus") if experience>10 else print("20% Bonus") if experience>5 else print("10% Bonus")