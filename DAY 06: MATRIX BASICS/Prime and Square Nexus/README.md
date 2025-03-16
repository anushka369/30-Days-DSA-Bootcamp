## Problem Statement

In a kingdom ruled by numbers, a matrix of size N×N represented the heart of the land. The matrix, filled with positive integers, had special rules:
- Prime Numbers: These guardians of wisdom were replaced by 0 but left no trace in their rows or columns.
- Perfect Squares: These symbols of balance had the power to mark their entire row and column with -1.

The kingdom's rulers needed to organize the matrix by applying these transformations and count:
- The number of rows fully transformed to -1.
- The number of prime numbers replaced with 0.

After processing the matrix, the rulers sought to present the transformed matrix and showcase the results of this magical process.

_Note: -1 will have high priority than 0._

## Input Format

- The first line contains a single integer N, the size of the matrix.
- The next N lines contain N integers each, representing the elements of the matrix.

## Output Format

- Print two integers: the count of rows fully marked as -1 and the count of prime numbers replaced with 0.
- Print the modified matrix with elements of the same row separated by a single space. Start the next row on a new line.

## Constraints

- 2 <= N <= 100
- 2 <= grid[i][j] <= 10^6

## Sample Testcase 0

### Testcase Input

4 <br>
2 6 4 8 <br>
5 9 12 15 <br>
10 11 18 7 <br>
20 21 25 16

### Testcase Output

3 0 <br>
-1 -1 -1 -1 <br>
-1 -1 -1 -1 <br>
10 -1 -1 -1 <br>
-1 -1 -1 -1

### Explanation

In the given matrix, the elements 2, 5, 11, 7 are prime, so replace them with 0. <br>
0 6 4 8 <br>
0 9 12 15 <br>
10 0 18 0 <br>
20 21 25 16 <br>

Now, 4, 9, 25 and 16 are perfect square, so replace the entire row and column with -1. <br>
-1 -1 -1 -1 <br>
-1 -1 -1 -1 <br>
10 -1 -1 -1 <br>
-1 -1 -1 -1

Since -1 have high priority than 0, so it has replace all 0s. <br>
Number of rows entirely marked as -1 = 3 <br>
Number of zeroes : 0 (we have to considered the final matrix after replacements)

## Sample Testcase 1

### Testcase Input

3 <br>
4 5 6 <br>
2 11 13 <br>
12 18 10

### Testcase Output

1 2 <br>
-1 -1 -1 <br>
-1 0 0 <br>
-1 18 10

### Explanation

In the given matrix, the elements 2, 5, 11 and 13 are prime, so replace them with 0.
4 0 6 <br>
0 0 0 <br>
12 18 10

Now, 4 is a perfect square, so replace the entire row and column with -1.
-1 -1 -1 <br>
-1 0 0 <br>
-1 18 10 <br>

Since -1 have high priority than 0, so it has replace the 0s present in (0,1) and (1,0).
<br> Number of rows entirely marked as -1 = 1 <br>
Number of zeroes : 2 (we have to considered the final matrix after replacements)

## Problem Link

[Click Here](https://unstop.com/courses/unstop-practice-interview-pep/30-days-dsa-bootcamp/day-matrix-basics-37742/coding-question-37745/)
