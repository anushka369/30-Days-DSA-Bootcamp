def is_subsequence(s, t):
    t_ptr = 0
    for char in s:
        if t_ptr < len(t) and char == t[t_ptr]:
            t_ptr += 1
          
    return t_ptr == len(t)

def find_first_day(S, T):
    current = S
    day = 1
    
    # Check up to a reasonable number of days
    while len(current) <= 10**6:  # Arbitrary large limit based on constraints
        if is_subsequence(current, T):
            return day
        
        # Next day: reverse current string and append S
        current = current[::-1] + S
        day += 1
    
    return -1  # If no solution found (shouldn't happen given problem constraints)

# Read input
S = input().strip()
T = input().strip()

# Print result
print(find_first_day(S, T))
