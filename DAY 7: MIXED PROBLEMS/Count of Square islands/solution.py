def count_squares(n, m, arr):
    # Initialize dp array with same dimensions as arr
    dp = [[0] * m for _ in range(n)]
    total = 0
    
    # Fill first row and column directly from arr
    for i in range(n):
        dp[i][0] = arr[i][0]
        total += dp[i][0]
      
    for j in range(1, m):
        dp[0][j] = arr[0][j]
        total += dp[0][j]
    
    # Fill dp array
    for i in range(1, n):
        for j in range(1, m):
            if arr[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                total += dp[i][j]
    
    return total

# Read input
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# Print result
print(count_squares(n, m, arr))
