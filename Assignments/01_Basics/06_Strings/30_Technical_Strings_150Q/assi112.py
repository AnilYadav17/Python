'''112. Find the minimum number of deletions to make a string palindrome.'''
# S = "aebcbda" -> 2
s = input("Enter string: ")

# Find the length of the Longest Palindromic Subsequence
n = len(s)
dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        if s[i] == s[j] and length == 2:
            dp[i][j] = 2
        elif s[i] == s[j]:
            dp[i][j] = dp[i+1][j-1] + 2
        else:
            dp[i][j] = max(dp[i+1][j], dp[i][j-1])

lps_length = dp[0][n-1] if n > 0 else 0
print("Minimum deletions =", n - lps_length)
