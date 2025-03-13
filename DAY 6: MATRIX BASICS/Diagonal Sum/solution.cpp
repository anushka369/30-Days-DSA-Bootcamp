#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int diagonal_sum(int n) 
{
    int total_sum = 2 * n; // Since every element in the matrix is 1, main and secondary diagonals each contribute 'n'
    
    // If N is odd, subtract the middle element (which is counted twice)
    if (n % 2 == 1) 
    {
        total_sum -= 1;
    }

    return total_sum;
}

int main() 
{
    int n;
    cin >> n;

    // Directly compute and print the diagonal sum without storing the matrix
    cout << diagonal_sum(n) << endl;
    
    return 0;
}
