## Problem Statement

Given a n * m matrix of ones and zeros, where 0 denotes water and 1 denotes island, now you have to count the total number of square submatrices that consist entirely of 1s. 

## Input Format

- First line contains n and m, where n is the number of rows and m is the column.
- From second line it contains the elements of the arr matrix.

## Output Format
Print the count of the number of square sub-island. 

## Constraints

- 1 <= arr.length <= 300
- 1 <= arr[0].length <= 300
- 0 <= arr[i][j] <= 1

## Sample Testcase 0

### Testcase Input

3 3 <br>
1 0 1 <br>
1 1 0 <br>
1 1 1

### Testcase Output
8

### Explanation

There are 7 squares of side 1. <br>
There are 1 squares of side 2. <br>
There is  0 square of side 3. <br>
Total number of squares = 7 + 1 + 0 = 8.

## Sample Testcase 1

### Testcase Input

3 3 <br>
1 0 1 <br>
1 1 0 <br>
1 1 0

### Testcase Output
7

### Explanation

There are 6 squares of side 1. <br>
There is 1 square of side 2. <br>
Total number of squares = 6 + 1 = 7.

## Problem Link

[Click Here](https://unstop.com/courses/unstop-practice-interview-pep/30-days-dsa-bootcamp/day-mixed-problems-37748/coding-question-37830/)
