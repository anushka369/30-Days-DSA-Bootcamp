#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

// Check if a number is prime
bool isPrime(int n) 
{
    if (n <= 1) 
    {
        return false;
    }
  
    if (n <= 3) 
    {
        return true;
    }
  
    if (n % 2 == 0 || n % 3 == 0)
    {
        return false;
    }
  
    for (int i = 5; i * i <= n; i += 6) 
    {
        if (n % i == 0 || n % (i + 2) == 0) 
        {
            return false;
        }
    }
  
    return true;
}

// Check if a number is perfect square
bool isPerfectSquare(int n) 
{
    int root = sqrt(n);
    return root * root == n;
}

void transform_matrix(vector<vector<int>>& matrix, int n, int& row_count, int& prime_count) 
{
    // Step 1: Replace primes with 0 and store perfect square positions
    vector<pair<int, int>> squares;
    prime_count = 0;
    
    for (int i = 0; i < n; i++) 
    {
        for (int j = 0; j < n; j++) 
        {
            if (isPrime(matrix[i][j])) 
            {
                matrix[i][j] = 0;
                prime_count++;
            }
              
            else if (isPerfectSquare(matrix[i][j])) 
            {
                squares.push_back({i, j});
            }
        }
    }
    
    // Step 2: For each perfect square, mark row and column with -1
    for (auto pos : squares) 
    {
        int row = pos.first;
        int col = pos.second;
        
        // Mark entire row
        for (int j = 0; j < n; j++) 
        {
            matrix[row][j] = -1;
        }
      
        // Mark entire column
        for (int i = 0; i < n; i++) 
        {
            matrix[i][col] = -1;
        }
    }
    
    // Step 3: Count rows with all -1s and remaining 0s
    row_count = 0;
    prime_count = 0;
    
    for (int i = 0; i < n; i++) 
    {
        bool all_minus_one = true;
        for (int j = 0; j < n; j++) 
        {
            if (matrix[i][j] == 0) 
            {
                prime_count++;
            }
          
            if (matrix[i][j] != -1) 
            {
                all_minus_one = false;
            }
        }
      
        if (all_minus_one) 
        {
            row_count++;
        }
    }
}

int main() 
{
    int n;
    cin >> n;
    vector<vector<int>> matrix(n, vector<int>(n));
  
    for (int i = 0; i < n; ++i) 
    {
        for (int j = 0; j < n; ++j) 
        {
            cin >> matrix[i][j];
        }
    }

    int row_count = 0;
    int prime_count = 0;
    transform_matrix(matrix, n, row_count, prime_count);

    cout << row_count << " " << prime_count << endl;
    for (const auto& row : matrix) 
    {
        for (int val : row) 
        {
            cout << val << " ";
        }
      
        cout << endl;
    }

    return 0;
}
