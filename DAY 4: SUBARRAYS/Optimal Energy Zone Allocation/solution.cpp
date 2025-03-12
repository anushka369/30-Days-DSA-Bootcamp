#include <iostream>
#include <vector>
using namespace std;

int countValidPartitions(vector<int>& E, int N) 
{
    int totalWays = 0;
    
    // Prefix sum array for efficient range sum calculation
    vector<int> prefixSum(N + 1, 0);
    for (int i = 0; i < N; ++i) 
    {
        prefixSum[i + 1] = prefixSum[i] + E[i];
    }
    
    // Iterate over possible sizes of Alpha (same as Gamma)
    for (int alphaSize = 1; alphaSize <= N / 2; ++alphaSize) 
    {
        int gammaStart = N - alphaSize; // Start of Gamma
        
        // Ensure there is a Beta section in between
        if (gammaStart <= alphaSize) 
        {
            break;
        }
        
        // Compute the sum of Alpha and Gamma
        int sumAlpha = prefixSum[alphaSize] - prefixSum[0];
        int sumGamma = prefixSum[N] - prefixSum[gammaStart];
        
        // Compute Beta range
        int sumBeta = prefixSum[gammaStart] - prefixSum[alphaSize];
        
        // Check if condition is met
        if (sumAlpha + sumGamma > sumBeta) 
        {
            totalWays++;
        }
    }
    
    return totalWays;
}

int main() 
{
    int N;
    cin >> N; // Read the number of plants

    vector<int> E(N);
    for (int i = 0; i < N; ++i) 
    {
        cin >> E[i];
    }

    int result = countValidPartitions(E, N);
    cout << result << endl;
    
    return 0;
}
