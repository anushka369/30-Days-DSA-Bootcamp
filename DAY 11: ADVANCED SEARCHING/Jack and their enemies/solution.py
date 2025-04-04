def min_k_to_kill_enemies(n, groups, m):
    total_enemies = sum(groups)
    low = 1
    high = total_enemies

    while low < high:
        mid = (low + high) // 2
        minutes_needed = 0

        for group in groups:
            minutes_needed += (group + mid - 1) // mid

        if minutes_needed > m:
            low = mid + 1
            
        else:
            high = mid
          
    return str(low) + ' ' + oct(low)[2:]

n = int(input())
groups = list(map(int, input().split()))

m = int(input())
print(min_k_to_kill_enemies(n, groups, m))
