#include <iostream>
#include <vector>
#include <set>
using namespace std;

vector<int> get_subarray_beauty(const vector<int>& nums, int k, int x) 
{
    vector<int> result;
    multiset<int> window_negatives; // Store only negative numbers in sorted order
    
    for (int i = 0; i < nums.size(); i++) 
    {
        // Insert negative numbers into multiset
        if (nums[i] < 0) 
        {
            window_negatives.insert(nums[i]);
        }

        // Maintain window size
        if (i >= k - 1) 
        {
            // If we have at least x negative numbers, find the x-th smallest
            if (window_negatives.size() >= x) 
            {
                auto it = window_negatives.begin();
                advance(it, x - 1); // Move iterator to x-th smallest element
                result.push_back(*it);
            } 
              
            else 
            {
                result.push_back(0);
            }

            // Remove the outgoing element from the multiset if it was negative
            if (nums[i - k + 1] < 0) 
            {
                window_negatives.erase(window_negatives.find(nums[i - k + 1]));
            }
        }
    }

    return result;
}

int main() 
{
    int k, x, n;
    cin >> k >> x >> n;
    
    vector<int> nums(n);
    for (int i = 0; i < n; ++i) 
    {
        cin >> nums[i];
    }
    
    vector<int> result = get_subarray_beauty(nums, k, x);    
    for (const auto& val : result) 
    {
        cout << val << " ";
    }
    
    return 0;
}
