import sys
input = sys.stdin.read

def main():
    s = list(map(int, input().strip().split()))

    if (sum(s) % 2 == 1):
        print("-1")
        return

    max_draws = (sum(s) - max(0, s[2] - s[0] - s[1])) // 2
    print(max_draws)

if __name__ == "__main__":
    main()
