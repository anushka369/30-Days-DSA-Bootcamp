## Problem Statement

You are given two sorted arrays a1 and a2 of size m and n respectively. 
Now we combine the values of these two arrays to make a mega array. 
The resulting mega array is also sorted in nature.
Your task is to find the median of this mega array.

## Input Format

Each Input has three lines, containing space-separated integers.
- The first line contains 2 values m and n respectively.
- The second line contains m numbers that signify nums1.
- The third line contains n numbers that signify nums2.

## Output Format
Return a Double data type number which is the median of two arrays.

## Constraints

- nums1.length == m
- nums2.length == n
- 0 <= m <= 10^6
- 0 <= n <= 10^6
- 1 <= m + n <= 2*10^6
- 10^4 <= nums1[i], nums2[i] <= 10^6

## Sample Testcase 0

### Testcase Input
2 1 <br>
1 3 <br>
2

### Testcase Output
2.0

### Explanation

Resulting array:- [1,2,3] <br>
Median of this array is 2.00000.

## Sample Testcase 1

### Testcase Input
2 2 <br>
1 3 <br>
2 4

### Testcase Output
2.5

### Explanation
Resulting array:- [1,2,3,4] <br>
Median of this array is ((2+3)/2) = 2.50000.

## Problem Link

[Click Here](https://unstop.com/courses/unstop-practice-interview-pep/30-days-dsa-bootcamp/day-advanced-searching-37798/coding-question-37803/)
