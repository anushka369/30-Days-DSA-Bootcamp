def is_prime(n):
    if n < 2:
        return False
      
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime_squares(limit):
    prime_squares = set()
    i = 2
  
    while i * i <= limit:
        if is_prime(i):
            prime_squares.add(i * i)
          
        i += 1
    return prime_squares

def qualifies(word):
    # Precompute prime squares up to 10^5 (max word length)
    prime_squares = generate_prime_squares(10**5)
    
    # Convert to lowercase
    word = word.lower()
    
    # Define vowels
    vowels = set('aeiou')
    
    # Count vowels and consonants
    vowel_count = 0
    consonant_count = 0
  
    for char in word:
        if char in vowels:
            vowel_count += 1
          
        else:
            consonant_count += 1
    
    # Check conditions
    if vowel_count < 2:  # Less than 2 vowels
        return "Disqualify"
      
    if consonant_count == 0:  # No consonants
        return "Disqualify"
      
    if consonant_count not in prime_squares:  # Not a prime square
        return "Disqualify"
    
    return "Qualify"

# Read input
word = input().strip()

# Print result
print(qualifies(word))
