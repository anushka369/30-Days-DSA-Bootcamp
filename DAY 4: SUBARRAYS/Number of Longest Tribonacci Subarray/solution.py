def generate_tribonacci_numbers(max_value):
    tribonacci = [0, 1, 1]
  
    while True:
        next_value = tribonacci[-1] + tribonacci[-2] + tribonacci[-3]
        if next_value > max_value:
            break
          
        tribonacci.append(next_value)
    return set(tribonacci)  # Return as a set for O(1) lookups

def count_tribonacci_subarrays(arr):
    MOD = 10**9 + 7
    max_value = 10**5
    tribonacci_set = generate_tribonacci_numbers(max_value)
    
    count = 0
    current_length = 0
    
    for num in arr:
        if num in tribonacci_set:
            current_length += 1
          
        else:
            if current_length > 0:
                count += (current_length * (current_length + 1)) // 2
                count %= MOD
              
            current_length = 0
    
    # If there was a valid segment at the end
    if current_length > 0:
        count += (current_length * (current_length + 1)) // 2
        count %= MOD
    
    return count

# Input reading
N = int(input())
arr = list(map(int, input().split()))

# Output the result
print(count_tribonacci_subarrays(arr))
