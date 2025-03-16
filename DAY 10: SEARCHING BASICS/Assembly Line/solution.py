def find_student_positions(n, heights, k, queries):
  
    """
    Parameters:
        1. n (int): Number of students
           heights (list): List of integers representing heights of students
        2. k (int): Number of queries
           queries (list): List of integers representing the height of the student that is enquired
           
    Returns:
        list: List of integers representing the 0-based index positions of the students for each query
    """
  
    def binary_search(arr, target):
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
              
            else:
                right = mid
        return left
    
    results = []
    for query in queries:
        # Find the position where query should be inserted or exists
        pos = binary_search(heights, query)
        results.append(pos)
    
    return results

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    idx = 0
    
    # First input is the integer n
    n = int(data[idx])
    idx += 1
    
    # Second input is the array of heights
    heights = list(map(int, data[idx:idx+n]))
    idx += n
    
    # Third input is the integer k
    k = int(data[idx])
    idx += 1
    
    # Next k inputs are the queries
    queries = list(map(int, data[idx:idx+k]))
    
    # Call user logic function
    results = find_student_positions(n, heights, k, queries)
    
    # Print the results
    for result in results:
        print(result)
        
if __name__ == "__main__":
    main()
