#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() 
{
    int N, M;
    
    // Read the number of suns and planets per sun
    cin >> N >> M;
    
    int max_moons = 0; // Variable to store the maximum moons in any solar system

    // Loop through each sun
    for (int i = 0; i < N; i++) 
    {
        int total_moons = 0; // Total moons for the current sun
        
        // Read the moons for each planet around the current sun
        for (int j = 0; j < M; j++) 
        {
            int moons;
            cin >> moons;
            total_moons += moons; // Accumulate total moons
        }
        
        // Update max_moons if current total is greater
        max_moons = max(max_moons, total_moons);
    }

    // Output the maximum moons in any solar system
    cout << max_moons << endl;
    
    return 0;
}
