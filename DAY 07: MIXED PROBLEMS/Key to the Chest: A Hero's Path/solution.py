from collections import deque

def shortest_path_to_chest(N, M, grid):
    # Find hero, chest, and keys
    hero_pos = None
    chest_pos = None
    keys = []
  
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'H':
                hero_pos = (i, j)
              
            elif grid[i][j] == 'C':
                chest_pos = (i, j)
              
            elif grid[i][j] == 'K':
                keys.append((i, j))
    
    total_keys = len(keys)
    if total_keys == 0:  # Edge case: no keys
        return bfs_simple(hero_pos, chest_pos, N, M, grid)
    
    # Directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # State: (row, col, keys_collected_mask)
    # Use bitmask to represent collected keys
    def bfs():
        queue = deque([(hero_pos[0], hero_pos[1], 0, 0)])  # (row, col, mask, steps)
        visited = set([(hero_pos[0], hero_pos[1], 0)])  # (row, col, mask)
        
        while queue:
            row, col, mask, steps = queue.popleft()
            curr_keys = bin(mask).count('1')
            
            # If at chest and all keys collected
            if (row, col) == chest_pos and curr_keys == total_keys:
                return steps
            
            # Explore all directions
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check bounds and obstacles
                if (0 <= new_row < N and 0 <= new_col < M and 
                    grid[new_row][new_col] != 'O'):
                    new_mask = mask
                    
                    # If we hit a key, update the mask
                    if grid[new_row][new_col] == 'K':
                        key_idx = keys.index((new_row, new_col))
                        new_mask |= (1 << key_idx)
                    
                    # Skip if we're at chest but haven't collected all keys
                    if (new_row, new_col) == chest_pos and bin(new_mask).count('1') != total_keys:
                        continue
                    
                    new_state = (new_row, new_col, new_mask)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_row, new_col, new_mask, steps + 1))
        
        return "Impossible"
    
    # Simple BFS for no-keys case
    def bfs_simple(start, end, N, M, grid):
        queue = deque([(start[0], start[1], 0)])  # (row, col, steps)
        visited = set([start])
        
        while queue:
            row, col, steps = queue.popleft()
            if (row, col) == end:
                return steps
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if (0 <= new_row < N and 0 <= new_col < M and 
                    grid[new_row][new_col] != 'O' and 
                    (new_row, new_col) not in visited):
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col, steps + 1))
                      
        return "Impossible"    
    return bfs()

# Read input
N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(input().split())

# Print result
print(shortest_path_to_chest(N, M, grid))
