#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Function to compute the maximum sum after partitioning
int max_sum_after_partitioning(vector<int>& arr, int k) 
{
    int n = arr.size();
    vector<int> dp(n + 1, 0); // DP table

    for (int i = 1; i <= n; i++) 
    {
        int max_val = 0;
        int best = 0;

        // Consider partitions of size 1 to K
        for (int j = 1; j <= k && i - j >= 0; j++) 
        {
            max_val = max(max_val, arr[i - j]); 
            best = max(best, dp[i - j] + max_val * j); 
        }
      
        dp[i] = best;
    }
    
    return dp[n];
}

// Function to count prime numbers ≤ n using the Sieve of Eratosthenes
int sieve_of_eratosthenes(int n) 
{
    if (n < 2) 
    {
        return 0; // No primes <= 1
    }
  
    vector<bool> is_prime(n + 1, true);
    is_prime[0] = is_prime[1] = false;
    
    for (int i = 2; i * i <= n; i++) 
    {
        if (is_prime[i]) 
        {
            for (int j = i * i; j <= n; j += i) 
            {
                is_prime[j] = false;
            }
        }
    }

    return count(is_prime.begin(), is_prime.end(), true);
}

int main() 
{
    int n, k;
    cin >> n;
    vector<int> arr(n);

    for (int i = 0; i < n; i++) 
    {
        cin >> arr[i];
    }

    cin >> k;    
    int max_sum = max_sum_after_partitioning(arr, k); // Get max sum
    int prime_count = sieve_of_eratosthenes(max_sum); // Get prime count

    cout << prime_count << endl;    
    return 0;
}
