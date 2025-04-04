def max_energy_level(P, Q):
    total_energy = 0
    
    for num in range(P, Q + 1):
        original = num
        reversed_num = int(str(num)[::-1])  # Reverse the digits
        total_energy += max(original, reversed_num)  # Add the maximum value
    
    return total_energy

# Input
P = int(input())  # Start of the range
Q = int(input())  # End of the range

# Output
print(max_energy_level(P, Q))
