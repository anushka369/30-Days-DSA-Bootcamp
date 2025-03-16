import sys

def find_lucky_stone_pairs(p, n, m, stones):
    # Step 1: Collect stones divisible by either N or M
    lucky_stones = []
    
    for stone in stones:
        if stone % n == 0 or stone % m == 0:
            lucky_stones.append(stone)

    # Step 2: Compute unique pairs
    count = 0
    k = len(lucky_stones)

    # Using combinatorial formula for pair counting: C(k, 2) = k * (k - 1) / 2
    count = (k * (k - 1)) // 2

    return count

def main():
    input = sys.stdin.read
    data = input().strip().split()

    p = int(data[0])  # Number of stones
    n = int(data[1])  # Special number N
    m = int(data[2])  # Special number M
  
    stones = list(map(int, data[3:]))  # List of stones

    # Call user logic function and print the output
    result = find_lucky_stone_pairs(p, n, m, stones)
    print(result)

if __name__ == "__main__":
    main()
