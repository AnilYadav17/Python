# Assignment 12: Expression Evaluation
# A gaming score system calculates bonus points using exponent and applies penalties using unary negative values and brackets.
# Input:
# 100 - (20 * (3**2)) + (40 / (+5)) - (-3)

result = 100 - (20 * (3**2)) + (40 / (+5)) - (-3)

# result = 100 - (20 * 9) + (40 / 5) - (-3)
# result = 100 - 180 + 8.0 - (-3)
# result = 100 - 180 + 8.0 + 3
# result = -80 + 8.0 + 3
# result = -72.0 + 3
# result = -69.0

print(result)
