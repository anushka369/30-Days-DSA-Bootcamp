def next_good_number(x):
  
    """
    Find the next number greater than x with all odd digits.
    
    Parameters:
        x (int): The input integer for the test case
        
    Returns:
        int: The next greatest good number
    """
  
    odd_digits = set('13579')  # Set of valid odd digits
    
    # Start checking from x + 1
    current = x + 1
    
    while True:
        # Convert current number to string to check its digits
        num_str = str(current)
      
        # Check if all digits are odd
        if all(digit in odd_digits for digit in num_str):
            return current
        current += 1

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    T = int(data[0])  # First input is the number of test cases
    results = []

    for i in range(1, T + 1):
        x = int(data[i])
        result = next_good_number(x)
        results.append(result)

    for res in results:
        print(res)

if __name__ == "__main__":
    main()
