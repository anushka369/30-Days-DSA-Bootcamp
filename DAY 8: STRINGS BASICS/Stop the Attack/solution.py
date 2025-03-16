def decipher_code(n, seq1, m, seq2):
    result = []
    i, j = 0, 0
    
    # Alternate characters while both sequences have characters
    while i < n and j < m:
        result.append(seq1[i])
        result.append(seq2[j])
      
        i += 1
        j += 1
    
    # Append remaining characters from seq1, if any
    while i < n:
        result.append(seq1[i])
        i += 1
    
    # Append remaining characters from seq2, if any
    while j < m:
        result.append(seq2[j])
        j += 1
    
    # Join characters into a single string
    return ''.join(result)

# Read input
n = int(input())
seq1 = input().strip()

m = int(input())
seq2 = input().strip()

# Print result
print(decipher_code(n, seq1, m, seq2))
