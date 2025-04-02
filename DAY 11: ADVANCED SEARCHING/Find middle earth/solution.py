def findMedianSortedArrays(nums1, nums2):
    # Ensure nums1 is the smaller array for efficient binary search
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1  

    m, n = len(nums1), len(nums2)
    left_size = (m + n + 1) // 2  # Total elements needed in the left partition
    low, high = 0, m  

    while low <= high:
        partitionA = (low + high) // 2
        partitionB = left_size - partitionA

        # Elements left and right of partition
        leftA = nums1[partitionA - 1] if partitionA > 0 else float("-inf")
        rightA = nums1[partitionA] if partitionA < m else float("inf")

        leftB = nums2[partitionB - 1] if partitionB > 0 else float("-inf")
        rightB = nums2[partitionB] if partitionB < n else float("inf")

        # Found correct partition
        if leftA <= rightB and leftB <= rightA:
            if (m + n) % 2 == 0:
                return (max(leftA, leftB) + min(rightA, rightB)) / 2.0
              
            else:
                return float(max(leftA, leftB))

        elif leftA > rightB:
            high = partitionA - 1  # Move left
          
        else:
            low = partitionA + 1  # Move right

# Input Handling
m, n = map(int, input().split())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

# Output the median
print(findMedianSortedArrays(nums1, nums2))
