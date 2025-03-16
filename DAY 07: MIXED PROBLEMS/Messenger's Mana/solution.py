from heapq import heappush, heappop
import sys

def min_mana_cost(grid, M, N):
    # Directions corresponding to runes
    directions = 
    {
        'a': (0, 1),  # right
        'b': (0, -1), # left
        'c': (1, 0),  # down
        'd': (-1, 0)  # up
    }
  
    all_moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # Cost to reach each cell: (row, col, cost)
    visited = set()  # To track visited states with minimum cost
    pq = [(0, 0, 0)]  # (cost, row, col)
    
    while pq:
        cost, row, col = heappop(pq)
        
        # If reached destination
        if row == M - 1 and col == N - 1:
            return cost
        
        # Skip if already visited with lower or equal cost
        if (row, col) in visited:
            continue
        visited.add((row, col))
        
        # Current rune direction
        curr_rune = grid[row][col]
        curr_dir = directions[curr_rune]
        
        # Try all possible moves
        for dr, dc in all_moves:
            new_row, new_col = row + dr, col + dc
            
            # Check if move is within grid
            if 0 <= new_row < M and 0 <= new_col < N:
                # Cost is 0 if following original rune, 1 if changing it
                new_cost = cost + (0 if (dr, dc) == curr_dir else 1)
                
                if (new_row, new_col) not in visited:
                    heappush(pq, (new_cost, new_row, new_col))
    
    return -1  # No path possible (shouldn't happen given problem constraints)

# Read input
M, N = map(int, input().split())
grid = []
for _ in range(M):
    grid.append(input().split())

# Print result
print(min_mana_cost(grid, M, N))
