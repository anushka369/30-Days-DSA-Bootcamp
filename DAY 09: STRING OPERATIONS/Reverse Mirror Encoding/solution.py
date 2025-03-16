def decode_message(S):
    # Create decoding map
    decode_map = {}
  
    # First half: a-n
    for i in range(14):  # 'a' (97) to 'n' (110)
        decode_map[chr(97 + i)] = chr(110 - i)  # a→n, b→m, ..., n→a
      
    # Second half: o#-z#
    for i in range(12):  # 'o' (111) to 'z' (122)
        decode_map[chr(111 + i) + '#'] = chr(122 - i)  # o#→z, p#→y, ..., z#→o
    
    # Decode the string
    result = []
    i = 0
  
    while i < len(S):
        # Check if current position has a '#'
        if i + 1 < len(S) and S[i + 1] == '#':
            token = S[i:i + 2]  # Take pair (e.g., 'o#')
            result.append(decode_map[token])
            i += 2
          
        else:
            token = S[i]  # Take single character
            result.append(decode_map[token])
            i += 1
    
    return ''.join(result)

# Read input
S = input().strip()

# Print result
print(decode_message(S))
