# Assignment 15: Expression Evaluation
# An electricity billing system uses nested brackets, exponent-based scaling, and unary corrections.
# Input:
# 60 + (12 * (2**3) // (+(4))) - (-(10 % 3))

result = 60 + (12 * (2**3) // (+(4))) - (-(10 % 3))

#result = 60 + (12 * 8 // 4) - ( -1))
#result = 60 + 24 + 1
#result = 85

print(result)
