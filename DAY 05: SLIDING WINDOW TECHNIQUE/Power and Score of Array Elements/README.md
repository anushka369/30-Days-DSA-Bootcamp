## Problem Statement

Given an array arr[] (0-based indexed) of integers of size N, define the power of the integer at index i as follows:

Let:
- a be the second minimum integer among all integers with indices less than i .
- b be the second minimum integer among all integers with indices greater than i.

The power of the integer at index i is defined as: `max(arr[i] - a, arr[i] - b).` <br>
The score of the array arr is defined as the sum of powers for all integers in the array. Print the score of the array arr.

_Note: If there are less than equal to one element before or after the index i, then consider the second minimus as INT_MAX._

## Input Format
- The first line contains an integer N which denotes the size of the array.
- The second line contains N space-separated integers denoting the elements of the array arr[].

## Output Format
Print an integer denoting the score of the array.

## Constraints

- 1 <= N <= 10^5
- 1 <= Arr[i] <= 10^6

## Sample Testcase 0

### Testcase Input
5 <br>
4 7 1 8 3

### Testcase Output
2

### Explanation

Index 0 (arr[0] = 4):
- Before: INT_MAX (no elements).
- After: Second minimum in [7, 1, 8, 3] = 3.
- Score: max(4 - INT_MAX, 4 - 3) = 1.

Index 1 (arr[1] = 7):
- Before: Second minimum in [4] = INT_MAX.
- After: Second minimum in [1, 8, 3] = 3.
- Score: max(7 - INT_MAX, 7 - 3) = 4.

Index 2 (arr[2] = 1):
- Before: Second minimum in [4, 7] = 7.
- After: Second minimum in [8, 3] = 8.
- Score: max(1 - 7, 1 - 8) = -6.

Index 3 (arr[3] = 8):
- Before: Second minimum in [4, 7, 1] = 4.
- After: INT_MAX (no elements).
- Score: max(8 - 4, 8 - INT_MAX) = 4.

Index 4 (arr[4] = 3):
- Before: Second minimum in [4, 7, 1, 8] = 4.
- After: INT_MAX (no elements).
- Score: max(3 - 4, 3 - INT_MAX) = -1.

Total Score: 1 + 4 - 6 + 4 - 1 = 2.

## Sample Testcase 1

### Testcase Input

4 <br>
3 8 1 6

### Testcase Output
-5

### Explanation

Index 0 (arr[0] = 3):
- Before: INT_MAX (no elements).
- After: Second minimum in [8, 1, 6] = 6.
- Score: max(3 - INT_MAX, 3 - 6) = -3.

Index 1 (arr[1] = 8):
- Before: Second minimum in [3] = INT_MAX.
- After: Second minimum in [1, 6] = 6.
- Score: max(8 - INT_MAX, 8 - 6) = 2.

Index 2 (arr[2] = 1):
- Before: Second minimum in [3, 8] = 8.
- After: Second minimum in [6] = INT_MAX.
- Score: max(1 - 8, 1 - INT_MAX) = -7.

Index 3 (arr[3] = 6):
- Before: Second minimum in [3, 8, 1] = 3.
- After: INT_MAX (no elements).
- Score: max(6 - 3, 6 - INT_MAX) = 3.

Total Score: -3 + 2 - 7 + 3 = -5.

## Problem Link

[Click Here](https://unstop.com/courses/unstop-practice-interview-pep/30-days-dsa-bootcamp/day-sliding-window-technique-37736/coding-question-37740/)
