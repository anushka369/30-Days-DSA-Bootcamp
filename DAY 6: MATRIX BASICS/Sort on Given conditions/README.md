## Problem Statement

A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until 
reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].
Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

## Input Format

- The first line contains two space-seperated integers, M and N, representing the number of rows and columns in the matrix.
- The next M lines each contain N space-seperated  integers, representing the elements of the matrix mat.Each line corresponds to a row in the matrix.

## Output Format
Print the Diagonally sorted matrix. Each row of the matrix should be printed on a new line, as space-seperated integers.

## Constraints

- 1 <= M, N <= 10^2
- 1 <= mat[i][j] <= 10^2

## Sample Testcase 0

### Testcase Input

3 4 <br>
3 3 1 1 <br>
2 2 1 2 <br>
1 1 2 2

### Testcase Output

2 1 1 1 <br>
1 2 2 2 <br>
1 2 3 3

### Explanation

Step-by-Step Sorting:
1. Diagonal starting at mat[0][0]: [3, 2, 2] → Sorted: [2, 2, 3]
2. Diagonal starting at mat[0][1]: [3, 1] → Sorted: [1, 3]
3. Diagonal starting at mat[0][2]: [1] → Sorted: [1]
4. Diagonal starting at mat[1][0]: [2, 1] → Sorted: [1, 2]
5. Diagonal starting at mat[2][0]: [1] → Sorted: [1]

## Sample Testcase 1

### Testcase Input

3 3 <br>
3 1 1 <br>
2 5 2 <br>
4 2 2

### Testcase Output

2 1 1 <br>
2 3 2 <br>
4 2 5

### Explanation

Step-by-Step Sorting:
1. Diagonal starting at mat[0][0]: [3, 5, 2] → Sorted: [2, 3, 5]
2. Diagonal starting at mat[0][1]: [1, 2] → Sorted: [1, 2]
3. Diagonal starting at mat[0][2]: [1] → Sorted: [1]
4. Diagonal starting at mat[1][0]: [2, 2] → Sorted: [2, 2]
5. Diagonal starting at mat[2][0]: [4] → Sorted: [4]

## Problem Link

[Click Here](https://unstop.com/courses/unstop-practice-interview-pep/30-days-dsa-bootcamp/day-matrix-basics-37742/coding-question-37746/)
