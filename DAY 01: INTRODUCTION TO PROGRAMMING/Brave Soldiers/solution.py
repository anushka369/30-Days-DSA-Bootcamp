import sys
import math

def sieve_of_eratosthenes(N):
    # Generates all prime numbers up to N using the Sieve of Eratosthenes
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

    for i in range(2, int(math.sqrt(N)) + 1):
        if is_prime[i]:
            for j in range(i * i, N + 1, i):
                is_prime[j] = False

    return is_prime

def count_brave_soldiers(N):
    # Counts numbers that are prime but not perfect squares
    is_prime = sieve_of_eratosthenes(N)
    brave_count = 0

    for i in range(2, N + 1):
        if is_prime[i] and int(math.sqrt(i)) ** 2 != i:  # Prime and not a perfect square
            brave_count += 1

    return brave_count    

def main():
    import sys
    input = sys.stdin.read
    n = int(input().strip())  # The input contains only one integer N
    
    # Call the user logic function and print the output
    result = count_brave_soldiers(n)
    print(result)

if __name__ == "__main__":
    main()
