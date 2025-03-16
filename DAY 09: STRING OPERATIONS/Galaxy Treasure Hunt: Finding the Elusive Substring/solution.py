from collections import Counter

def shortest_substring(S, T):
    if len(S) < len(T):
        return -1
    
    # Frequency of characters in T
    t_count = Counter(T)
    required = len(t_count)  # Number of unique characters to match
    
    # Frequency of characters in current window
    window_count = {}
    formed = 0  # Number of characters matched with required frequency
    
    # Initialize window pointers and result
    left = right = 0
    min_len = float('inf')
    min_left = min_right = 0
    
    while right < len(S):
        # Add character from right to window
        char = S[right]
        window_count[char] = window_count.get(char, 0) + 1
        
        # Check if this character contributes to matching T
        if char in t_count and window_count[char] == t_count[char]:
            formed += 1
        
        # Try to shrink window from left
        while left <= right and formed == required:
            char = S[left]
            
            # Update minimum length
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_left, min_right = left, right
            
            # Remove character from left
            window_count[char] -= 1
            if char in t_count and window_count[char] < t_count[char]:
                formed -= 1
            left += 1
        
        right += 1
    
    if min_len != float('inf'):
        return min_len
      
    else:
        return -1

# Read input
S = input().strip()
T = input().strip()

# Print result
print(shortest_substring(S, T))
