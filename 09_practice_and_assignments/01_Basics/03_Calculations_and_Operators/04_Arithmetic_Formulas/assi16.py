# Assignment 16: Expression Evaluation
# A performance evaluation system calculates final score using grouped operations, exponent, division, and unary adjustments.
# Input:
# 45 + (15 * (2**2)) - (20 / (+(5))) + (-(7 % 3))

result = 45 + (15 * (2**2)) - (20 / (+(5))) + (-(7 % 3))

#result = 45 + (15 * 4) -(20 / 5) + (-1)
#result = 45 + 60 - 4 - 1
#result = 100

print(result)
