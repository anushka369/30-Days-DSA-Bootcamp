#include <iostream>
#include <vector>
#include <limits.h>
using namespace std;

int computeScore(vector<int>& arr) 
{
    int n = arr.size();
    vector<int> left_min(n, INT_MAX), left_second_min(n, INT_MAX);
    vector<int> right_min(n, INT_MAX), right_second_min(n, INT_MAX);
    
    int min1 = INT_MAX, min2 = INT_MAX;

    // Compute first and second minimum from the left
    for (int i = 0; i < n; i++) 
    {
        left_min[i] = min1;
        left_second_min[i] = min2;

        if (arr[i] < min1) 
        {
            min2 = min1;
            min1 = arr[i];
        } 
          
        else if (arr[i] < min2 && arr[i] != min1) 
        {
            min2 = arr[i];
        }
    }

    min1 = INT_MAX, min2 = INT_MAX;

    // Compute first and second minimum from the right
    for (int i = n - 1; i >= 0; i--) 
    {
        right_min[i] = min1;
        right_second_min[i] = min2;

        if (arr[i] < min1) 
        {
            min2 = min1;
            min1 = arr[i];
        } 
          
        else if (arr[i] < min2 && arr[i] != min1) 
        {
            min2 = arr[i];
        }
    }

    int score = 0;

    // Calculate the final score
    for (int i = 0; i < n; i++) 
    {
        int a = (i > 0) ? left_second_min[i] : INT_MAX;
        int b = (i < n - 1) ? right_second_min[i] : INT_MAX;

        int power = max(arr[i] - a, arr[i] - b);
        score += power;
    }

    return score;
}

int main() 
{
    int n;
    cin >> n;
    vector<int> arr(n);
  
    for (int i = 0; i < n; i++) 
    {
        cin >> arr[i];
    }

    cout << computeScore(arr) << endl;
    return 0;
}
