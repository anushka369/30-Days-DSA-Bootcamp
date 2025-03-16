## Problem Statement

You are given an integer array of size N. Your task is to partition this array into contiguous subarrays, where each subarray contains at most K elements. 
After partitioning, replace every element in each subarray with the largest value from that subarray.
Next, calculate the maximum possible sum of the transformed array. Let this maximum sum be M.
Finally, find and display the count of prime numbers that are less than or equal to M.
Test cases are generated such that the answer fits within a 32-bit integer.

## Input Format

- The first line contains an integer N, which represents the size of the array.
- The second line contains N space-separated integers representing the elements of the array.
- The third line contains an integer K, which is the maximum allowed size for each subarray.

## Output Format
Print a single integer, representing the count of prime numbers less than or equal to M, where  M is the maximum sum after partitioning the array.

## Constraints

- 1 <= Arr.length <= 5 * 10^2
- 0 <= Arr[i] <= 10^6
- 1 <= K <= Arr.length

## Sample Testcase 0

### Testcase Input

7 <br>
1 15 7 9 2 5 10 <br>
3

### Testcase Output
23

### Explanation

Split the array [1, 15, 7, 9, 2, 5, 10] into contiguous subarrays of length up to 3.

- Subarray 1: [1, 15, 7] <br>
  After transformation: [15, 15, 15]
  
- Subarray 2: [2, 5, 10] <br>
  After transformation: [10, 10, 10]
  
- Subarray 3: [9] <br>
  After transformation: [9]

Overall sum = 15 + 15 + 15 + 10 + 10 + 10 + 9 = 84
<br> Number of Primes less than equal to 84 = 23

## Sample Testcase 1

### Testcase Input
1 <br>
1 <br>
1

### Testcase Output
0

### Explanation
The array contains only one element, so the maximum sum after partitioning is 1. <br>
The count of prime numbers less than or equal to 1 is 0, as there are no primes less than or equal to 1.

## Problem Link

[Click Here](https://unstop.com/courses/unstop-practice-interview-pep/30-days-dsa-bootcamp/day-sliding-window-technique-37736/coding-question-37741/)
