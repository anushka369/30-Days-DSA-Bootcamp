#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

void diagonal_sort(vector<vector<int>>& mat) 
{
    int m = mat.size(), n = mat[0].size();
    map<int, vector<int>> diagonals;

    // Store all diagonals in a map
    for (int i = 0; i < m; ++i) 
    {
        for (int j = 0; j < n; ++j) 
        {
            diagonals[i - j].push_back(mat[i][j]);
        }
    }

    // Sort each diagonal
    for (auto& diag : diagonals) 
    {
        sort(diag.second.begin(), diag.second.end());
    }

    // Put sorted diagonals back into the matrix
    for (int i = 0; i < m; ++i) 
    {
        for (int j = 0; j < n; ++j) 
        {
            mat[i][j] = diagonals[i - j].front();
            diagonals[i - j].erase(diagonals[i - j].begin());
        }
    }
}

int main() 
{
    int m, n;
    cin >> m >> n;
    vector<vector<int>> mat(m, vector<int>(n));

    // Input matrix
    for (int i = 0; i < m; ++i) 
    {
        for (int j = 0; j < n; ++j) 
        {
            cin >> mat[i][j];
        }
    }

    // Sort diagonals
    diagonal_sort(mat);

    // Output sorted matrix
    for (const auto& row : mat) 
    {
        for (const auto& element : row) 
        {
            cout << element << " ";
        }
        cout << endl;
    }

    return 0;
}
