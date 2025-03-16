#include <iostream>
#include <vector>
#include <deque>
using namespace std;

vector<int> find_tallest(int N, int K, vector<int> height) 
{
    vector<int> result;
    deque<int> dq; // Stores indices of elements in current window

    for (int i = 0; i < N; i++) 
    {
        // Remove elements from the front if they are out of the window
        if (!dq.empty() && dq.front() <= i - K) 
        {
            dq.pop_front();
        }

        // Remove elements from the back if they are smaller than current element
        while (!dq.empty() && height[dq.back()] <= height[i]) 
        {
            dq.pop_back();
        }

        // Add current element index to the deque
        dq.push_back(i);

        // Start adding maximums to the result once we reach the first valid window
        if (i >= K - 1) 
        {
            result.push_back(height[dq.front()]);
        }
    }

    return result;
}

int main() 
{
    int N, K;
    cin >> N >> K;
  
    vector<int> height(N);
    for (int i = 0; i < N; i++) 
    {
        cin >> height[i];
    }

    vector<int> result = find_tallest(N, K, height);
    for (int i = 0; i < result.size(); i++) 
    {
        cout << result[i] << " ";
    }

    cout << endl;
    return 0;
}
