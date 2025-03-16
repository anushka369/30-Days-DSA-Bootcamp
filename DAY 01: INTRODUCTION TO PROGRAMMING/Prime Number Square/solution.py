import sys

#Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False

    if n in (2, 3):
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

# Function to find the N-th term in Alice's sequence
def nth_alice_choice(N):
    prime_count = 0
    num = 2

    while True:
        if is_prime(num):
            prime_count += 1
            
            if prime_count == N:
                return num * num
        num += 1

# Read input
N = int(sys.stdin.read().strip())

# Compute and print the result
print(nth_alice_choice(N))
