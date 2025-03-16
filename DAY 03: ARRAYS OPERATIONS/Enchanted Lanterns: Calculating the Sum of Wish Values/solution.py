def calculate_wish_values_sum(N, A):

    # Precompute maximum values from the current peak to the highest point
    max_right = [0] * N
    max_right[N - 1] = A[N - 1]
    
    for i in range(N - 2, -1, -1):
        max_right[i] = max(A[i], max_right[i + 1])

    # Compute the sum of wish values using a running minimum
    min_left = float('inf')
    wish_values_sum = 0

    for i in range(N):
        min_left = min(min_left, A[i])  # Update minimum from the start to current peak
        wish_values_sum += abs(max_right[i] - min_left)

    return wish_values_sum

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    N = int(data[0])  # First input is the integer N
    A = list(map(int, data[1:]))  # Remaining input is the array of brightness values
    
    # Call user logic function and print the output
    result = calculate_wish_values_sum(N, A)
    print(result)

if __name__ == "__main__":
    main()
