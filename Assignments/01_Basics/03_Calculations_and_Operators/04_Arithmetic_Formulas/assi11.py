'''Assignment 11: Expression Evaluation

A billing system applies nested calculations with discounts and extra charges using brackets and unary operators.

Input:
50 + (10 * (+(2**3))) / 4 - (-6 % 4)'''

result = 50 + (10 * (+(2**3))) / 4 - (-6 % 4)

# result = 50 + (10 * (+(8))) / 4 - (-6 % 4)
# result = 50 + (10 * 8) / 4 - (-6 % 4)
# result = 50 + 80 / 4 - (-6 % 4)
# result = 50 + 20.0 - (-6 % 4)

# result = 50 + 20.0 - (2)      # because -6 % 4 = 2
# result = 50 + 20.0 - 2
# result = 70.0 - 2
# result = 68.0

print(result)
