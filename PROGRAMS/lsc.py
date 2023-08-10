def longest_common_subsequence_length(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a 2D DP table to store LCS lengths
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table using bottom-up approach
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The length of LCS is stored in dp[m][n]
    return dp[m][n]


str1 = input("Enter first string = ")
str2 = input("Enter second string = ")

print("Length of LCS is :  ", longest_common_subsequence_length(str1, str2))
