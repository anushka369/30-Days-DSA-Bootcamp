#include <iostream>
#include <vector>
using namespace std;

void can_partition_chocolates(int n, vector<int>& chocolates) 
{
    // Calculate total sum
    long long total_sum = 0;
    for (int i = 0; i < n; i++) 
    {
        total_sum += chocolates[i];
    }
    
    // If total sum is odd, equal partition is impossible
    if (total_sum % 2 != 0) 
    {
        cout << "NO" << endl;
        return;
    }
    
    // Target sum for each partition
    int target = total_sum / 2;
    
    // Create DP array
    // dp[j] represents whether sum j is possible using some bags
    vector<bool> dp(target + 1, false);
    dp[0] = true;  // Sum 0 is always possible (empty subset)
    
    // For each chocolate bag
    for (int i = 0; i < n; i++) 
    {
        // Update dp array from right to left
        for(int j = target; j >= chocolates[i]; j--) 
        {
            dp[j] = dp[j] || dp[j - chocolates[i]];
        }
    }
    
    // If target sum is achievable
    if (dp[target]) 
    {
        cout << "YES" << endl;
    } 
    
    else 
    {
        cout << "NO" << endl;
    }
}

int main() 
{
    int n;
    cin >> n;
    vector<int> chocolates(n);
  
    for (int i = 0; i < n; ++i) 
    {
        cin >> chocolates[i];
    }
  
    can_partition_chocolates(n, chocolates);
    return 0;
}
