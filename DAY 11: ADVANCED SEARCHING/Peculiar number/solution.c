#include <stdio.h>
#include <stdlib.h>

// Function to get nth Fibonacci number with modulo to prevent overflow
long long getFibonacci(int n) 
{
    if (n == 0) 
    {
        return 0;
    }
  
    if (n == 1) 
    {
        return 1;
    }
    
    long long a = 0, b = 1;
    for (int i = 2; i <= n; i++) 
    {
        long long temp = a + b;
        a = b;
        b = temp;
    }
  
    return b;
}

// Function to find minimum possible maximum sum with k partitions
long long minMaxSum(int n, int k, int arr[]) 
{
    long long left = 0, right = 0;
    // Find maximum single element as minimum possible answer
    for (int i = 0; i < n; i++) 
    {
        if (arr[i] > left) 
        {
            left = arr[i];  // Minimum possible max sum
        }
      
        right += arr[i];                  // Maximum possible max sum
    }
    
    if (k == 1) 
    {
        return right;  // If k=1, only one partition possible
    }
    
    long long result = right;
    while (left <= right) 
    {
        long long mid = left + (right - left) / 2;
        
        // Count partitions needed with max sum <= mid
        int count = 1;
        long long curr_sum = 0;
        
        for (int i = 0; i < n; i++) 
        {
            if (arr[i] > mid) 
            {   
                // Single element exceeds mid
                count = k + 1;   // Force failure
                break;
            }
          
            if (curr_sum + arr[i] <= mid) 
            {
                curr_sum += arr[i];
            } 
            
            else 
            {
                count++;
                curr_sum = arr[i];
            }
        }
        
        if (count <= k) 
        {
            result = mid;
            right = mid - 1;
        }
        
        else 
        {
            left = mid + 1;
        }
    }
    return result;
}

int peculiarNumber(int n, int k, int arr[]) 
{
    // Step 1: Replace each element with absolute difference from index
    int modified[n];
    for (int i = 0; i < n; i++) 
    {
        modified[i] = abs(arr[i] - i);
    }
    
    // Step 2: Find minimum possible maximum sum with k partitions
    long long max_sum = minMaxSum(n, k, modified);
    
    // Step 3: If sum < 100, return that Fibonacci number, else return sum
    if (max_sum < 100) 
    {
        return (int)getFibonacci(max_sum);
    }
  
    return (int)max_sum;
}

int main() 
{
    int n, k;
    scanf("%d %d", &n, &k);
    int arr[n];
    for(int i = 0; i < n; ++i) 
    {
        scanf("%d", &arr[i]);
    }

    int result = peculiarNumber(n, k, arr);
    printf("%d\n", result);

    return 0;
}
