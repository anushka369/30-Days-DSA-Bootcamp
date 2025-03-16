def count_unique_substrings(S, K):
    n = len(S)
    result = []
    
    # For each length from 2 to K
    for length in range(2, K + 1):
        count = 0
      
        # Slide window of size 'length' across string
        for i in range(n - length + 1):
            substring = S[i:i + length]
          
            # Check if all characters are unique
            if len(set(substring)) == length:
                count += 1
        result.append(count)
    
    # Print results
    for count in result:
        print(count)

# Read input
S = input().strip()
K = int(input())

# Process and output
count_unique_substrings(S, K)
