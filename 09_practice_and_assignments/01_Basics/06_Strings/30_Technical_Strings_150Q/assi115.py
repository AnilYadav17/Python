'''115. Find the edit distance (Levenshtein distance) between two strings.'''
# S1 = "kitten", S2 = "sitting" -> 3
s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")

m = len(s1)
n = len(s2)

dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(m + 1):
    for j in range(n + 1):
        if i == 0:
            dp[i][j] = j
        elif j == 0:
            dp[i][j] = i
        elif s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = 1 + min(dp[i][j-1],    # Insert
                               dp[i-1][j],    # Remove
                               dp[i-1][j-1])  # Replace

print("Edit Distance =", dp[m][n])
