from collections import Counter

def validate_password(password):
    freq = Counter(password)  # Count occurrences of each element
    
    has_exactly_two = False  # Flag to check if at least one element appears exactly twice
    
    for count in freq.values():
        if count % 2 != 0:  # If any element has an odd frequency, return INVALID
            return ("INVALID", min(freq, key=lambda x: (-freq[x], x)))  
          
        if count == 2:
            has_exactly_two = True

    # If no number appears exactly twice, return INVALID
    if not has_exactly_two:
        return ("INVALID", min(freq, key=lambda x: (-freq[x], x)))
    
    # Find the most frequent element (smallest in case of ties)
    most_frequent = min(freq, key=lambda x: (-freq[x], x))
    
    return ("VALID", most_frequent)


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    N = int(data[0])  # First input is the integer N
    password = list(map(int, data[1:]))  # Remaining input is the password array
    
    # Call user logic function
    validation_result, most_frequent_element = validate_password(password)
    
    # Print the output
    print(validation_result)
    print(most_frequent_element)

if __name__ == "__main__":
    main()
