def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def collect_fruits(M, N, grid):
    result = []
    
    for i in range(M):
        # Determine direction based on row index
        if i % 2 == 0:  # Even rows (0-based): left to right
            for j in range(N):
                if not is_prime(grid[i][j]):
                    result.append(grid[i][j])
                  
        else:  # Odd rows: right to left
            for j in range(N - 1, -1, -1):
                if not is_prime(grid[i][j]):
                    result.append(grid[i][j])
    
    # If no non-prime numbers found, return -1
    if not result:
        return "-1"
    return " ".join(map(str, result))

# Read input
M, N = map(int, input().split())
grid = []
for _ in range(M):
    grid.append(list(map(int, input().split())))

# Print result
print(collect_fruits(M, N, grid))
