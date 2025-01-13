def charge(arr):
    while arr and arr[-1] < 0:
        arr.pop()
    while arr and arr[0] < 0:
        del arr[0]

    n = len(arr)
    if n == 1:
        return arr[0]

    # DP table
    dp = [[0] * n for _ in range(n)]

    # Base case: Single elements
    for i in range(n):
        dp[i][i] = arr[i]

    # Fill DP table
    for length in range(2, n + 1):  # Subarray lengths
        for i in range(n - length + 1):  # Starting index
            j = i + length - 1  # Ending index
            dp[i][j] = max(dp[i][j], dp[i + 1][j])  # Remove leftmost
            dp[i][j] = max(dp[i][j], dp[i][j - 1])  # Remove rightmost
            for k in range(i + 1, j):  # Remove middle element
                dp[i][j] = max(dp[i][j], dp[i][k - 1] + dp[k + 1][j])

    return dp[0][n - 1]


print(charge([1,2,3,5,7,9,-10,2])) #18
print(charge([-10,5,2,5,-10]))  #10
print(charge([1,1,1,1,1,-8,-8,-8,1,1,1])) #3
print(charge([5,5,5])) #10
print(charge([5,-4,5,5,-4,5]))#10