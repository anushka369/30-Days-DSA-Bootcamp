def calculate_min_moves(seats, students):
    """
    Calculates the minimum number of moves required to move each student to a seat.

    Parameters:
        seats (list): List of integers representing the positions of seats
        students (list): List of integers representing the positions of students

    Returns:
        int: Minimum number of moves required to move each student to a seat
    """
    # Sort both lists to ensure optimal pairing
    seats.sort()
    students.sort()
    
    # Compute the sum of absolute differences between corresponding elements
    return sum(abs(seats[i] - students[i]) for i in range(len(seats)))

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    seats = list(map(int, data[1:n+1]))
    students = list(map(int, data[n+1:2*n+1]))
    
    # Call user logic function and print the output
    result = calculate_min_moves(seats, students)
    print(result)

if __name__ == "__main__":
    main()
