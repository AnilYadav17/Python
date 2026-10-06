'''125. Find the shortest common supersequence of two strings.'''
# S1 = "AGGTAB", S2 = "GXTXAYB" -> "AGGXTXAYB"
s1 = input("Enter String 1: ")
s2 = input("Enter String 2: ")

m, n = len(s1), len(s2)
dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# Reconstruct the supersequence string
scs = ""
i, j = m, n
while i > 0 and j > 0:
    if s1[i-1] == s2[j-1]:
        scs = s1[i-1] + scs
        i -= 1
        j -= 1
    elif dp[i-1][j] > dp[i][j-1]:
        scs = s1[i-1] + scs
        i -= 1
    else:
        scs = s2[j-1] + scs
        j -= 1

while i > 0:
    scs = s1[i-1] + scs
    i -= 1
while j > 0:
    scs = s2[j-1] + scs
    j -= 1

print("Shortest Common Supersequence =", scs)
