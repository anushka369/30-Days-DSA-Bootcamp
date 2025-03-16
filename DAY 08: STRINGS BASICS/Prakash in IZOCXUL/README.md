## Problem Statement

Prakash had a dream about a planet named IZOCXUL, where only lowercase letters exist. 
He gave you a string S from that planet, and your task is to find how many substrings of length 2 to K consist of unique characters only.

## Input Format

- The first line contains a string S, representing the string from this planet.
- The Second line consists of an integer K.

## Output Format
Print K-1 lines where each line denotes the count of substring of size, from 2 to K.

## Constraints

- |S| <= 10^3
- 2 <= K <= |S|

_NOTE :_ |S| denotes the length of the string.

## Sample Testcase 0

### Testcase Input

aabce
<br> 4

### Testcase Output

3 <br>
2 <br>
1

### Explanation

Given K = 4 and string - 'aabce' <br>
Substring of length 2 with unique characters are {(ab), (bc), (ce)}. Count = 3
<br> Substring of length 3 with unique characters are {(abc), (bce)}. Count = 2
<br> Substring of length 4 with unique characters is {(abce)}. Count = 1

## Sample Testcase 1

### Testcase Input

abc
<br> 3

### Testcase Output

2 <br>
1

### Explanation

Given K = 3 and string - 'abc' <br>
Substrgin of length 2 with unique characters are {(ab), (bc)}. Count = 2
<br> Substrgin of length 3 with unique characters is {(abc)}. Count = 1

## Problem Link 

[Click Here](https://unstop.com/courses/unstop-practice-interview-pep/30-days-dsa-bootcamp/day-strings-basics-37781/coding-question-37783/)
