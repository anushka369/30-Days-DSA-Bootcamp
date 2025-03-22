#include <stdio.h>

// Comparison function for quick sort
int compare(const void* a, const void* b) 
{
    return (*(int*)a - *(int*)b);
}

// Count elements <= target in sorted array using binary search
int count_less_equal(int arr[], int size, int target) 
{
    if (size == 0) 
    {  
        return 0;
    }
  
    if (target < arr[0]) 
    { 
        return 0;
    }
  
    if (target >= arr[size-1]) 
    {  
        return size;
    }
    
    int left = 0, right = size - 1;
    while (left <= right) 
    {
        int mid = (left + right) / 2;
        if (arr[mid] <= target) 
        {
            left = mid + 1;
        } 
        
        else 
        {
            right = mid - 1;
        }
    }
    return left;
}

int user_logic(int n, int arr[], int b[]) 
{
    // Create sorted copies
    int sorted_arr[n], sorted_b[n];
    for (int i = 0; i < n; i++) 
    {
        sorted_arr[i] = arr[i];
        sorted_b[i] = b[i];
    }
    
    // Sort the copies
    qsort(sorted_arr, n, sizeof(int), compare);
    qsort(sorted_b, n, sizeof(int), compare);
    
    // Calculate interest value for syllabus 1
    long long interest1 = 0;
    for (int i = 0; i < n; i++) 
    {
        interest1 += count_less_equal(sorted_b, n, arr[i]);
    }
    
    // Calculate interest value for syllabus 2
    long long interest2 = 0;
    for (int i = 0; i < n; i++) 
    {
        interest2 += count_less_equal(sorted_arr, n, b[i]);
    }
    
    // Return the maximum
    if (interest1 > interest2)
    {
        return interest1;
    }
      
    else
    {
        return interest2;
    }
}

int main()
{
    int n;
    scanf("%d", &n);
    int arr[n], b[n];
  
    for (int i = 0; i < n; i++) 
    {
        scanf("%d", &arr[i]);
    }
  
    for (int i = 0; i < n; i++) 
    {
        scanf("%d", &b[i]);
    }
  
    int result = user_logic(n, arr, b);
    printf("%d\n", result);
  
    return 0;
}
