import sys

input = sys.stdin.read

def min_delivery_time(n, m, p, unstoppables, spells):
    unstoppables.sort()
    spells.sort()

    def is_possible(time):
        i, j = 0, 0  # Pointers for unstoppables and spells
      
        while i < n and j < m:
            if abs(unstoppables[i] - spells[j]) + abs(spells[j] - p) <= time:
                i += 1  # Assign this spell to this unstoppable
              
            j += 1  # Move to the next spell
        
        return i == n  # All unstoppables must be matched

    # Binary search for minimum maximum time
    left, right = 0, max(max(unstoppables), max(spells), p) * 2
  
    while left < right:
        mid = (left + right) // 2
      
        if is_possible(mid):
            right = mid
          
        else:
            left = mid + 1

    return left

if __name__ == "__main__":
    data = input().strip().split()
  
    n = int(data[0])
    m = int(data[1])
    p = int(data[2])
  
    unstoppables = list(map(int, data[3:3+n]))
    spells = list(map(int, data[3+n:]))
  
    result = min_delivery_time(n, m, p, unstoppables, spells)
    print(result)
