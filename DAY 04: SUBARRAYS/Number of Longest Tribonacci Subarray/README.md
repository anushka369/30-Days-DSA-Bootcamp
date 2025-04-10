## Problem Statement

Alice is given an array of non-negative integers containing N elements. Your task is to return the total number of subarrays that contain only Tribonacci numbers.
Tribonacci numbers are defined by the Tribonacci Series: The first three numbers are 0, 1, 1. <br> <br> Each subsequent number is the sum of the previous three numbers, 
i.e., the Nth number is calculated as: <br> Tribonacci (N) = Tribonacci (N − 1) + Tribonacci (N − 2) + Tribonacci (N − 3). <br>
To avoid integer overflow, take the result modulo 10^9 + 7.

## Input Format

- The first line contains an integer N, representing the size of the array,
- The second line contains N space-separated integer, representing the array arr.

## Output Format

Return the total number of subarrays that consist solely of Tribonacci numbers.

## Constraints

- 1 ≤ N ≤ 10^5
- 1 ≤ arr[i] ≤ 10^5

## Sample Testcase 0

### Testcase Input

5 <br>
0 1 1 2 4 

### Testcase Output
15

### Explanation
The total number of Tribonacci subarrays is 15: [0], [0,1], [0,1,1], [0,1,1,2], [0,1,1,2,4], [1], [1,1], [1,1,2], [1,1,2,4], [1], [1,2], [1,2,4], [2], [2,4], [4]

## Sample Testcase 1

### Testcase Input

5 <br>
0 1 1 105 3

### Testcase Output
6

### Explanation
The total number of Tribonacci subarrays is 6: [0], [0,1], [0,1,1], [1], [1,1], [1] <br>
(Note that numbers 105 and 3 are not Tribonacci numbers, so they break the valid subarrays)

## Problem Link

[Click Here](https://unstop.com/courses/unstop-practice-interview-pep/30-days-dsa-bootcamp/day-subarrays-37731/coding-question-37732/)
