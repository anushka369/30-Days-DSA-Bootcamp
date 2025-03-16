def process_string(S):
    first_char = S[0]  # Store original first character
    S = S.lower()      # Convert to lowercase
    
    if S == S[::-1]:
        return len(S)
      
    else:
        return ord(first_char)  # Use original first character

# Read input
S = input().strip()

# Print result
print(process_string(S))
