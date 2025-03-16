from collections import Counter

def process_frequencies(s):
    # Count frequencies
    freq = Counter(s)
    
    # Get characters with odd frequencies
    odd_freq = [(char, count) for char, count in freq.items() if count % 2 == 1]
    
    # Sort by frequency (descending) and then alphabetically (ascending)
    odd_freq.sort(key=lambda x: (-x[1], x[0]))
    
    # Case handling
    if len(odd_freq) == 0:
        print(-1)
      
    elif len(odd_freq) < 3:
        # Find smallest odd frequency, lexicographically smallest char
        min_freq = min(odd_freq, key=lambda x: (x[1], x[0]))
        print(f"{min_freq[0]} {min_freq[1]}")
      
    else:
        # Take top 3 (or all if exactly 3)
        top_three = odd_freq[:3]
        product = 1
      
        for char, count in top_three:
            print(f"{char} {count}")
            product *= count
        print(product)

# Read input
s = input().strip()

# Process and output
process_frequencies(s)
