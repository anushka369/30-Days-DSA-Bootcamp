## Problem Statement

There are N suns in a galaxy, each sun has M planets, each of the M planets have some number of moons, 
denoted by galaxy(i)(j), which is the number of moons of the jth planet having the ith sun.
Your task is to determine the maximum number of moons in any solar system. 
For each sun, calculate the total number of moons across all its planets, and output the highest total number of moons found in a single solar system.

## Input Format

- The first line of input contains two space-separated integers, N and M, representing the number of suns and the number of planets per sun, respectively.
- The next N lines of input contains M space separated integers, representing the number of moons for each planet around the respective sun.

## Output Format
Display a single integer denoting the maximum total number of moons in a solar system (i.e., across all planets orbiting the same sun).

## Constraints

- 1 <= N <= 5 * 10^2
- 1 <= M <= 5 * 10^2
- 1 <= galaxy(i)(j) <= 10^4

## Sample Testcase 0

### Testcase Input

2 3 <br>
1 2 3 <br>
4 5 6

### Testcase Output
15

### Explanation
The second sun has 3 planets and the total of their moons is 15.

## Sample Testcase 1

### Testcase Input

1 1 <br>
5

### Testcase Output
5

### Explanation
There is only 1 sun and 1 planet having 5 moons.

## Problem Link

[Click Here](https://unstop.com/courses/unstop-practice-interview-pep/30-days-dsa-bootcamp/day-matrix-basics-37742/coding-question-37744/)
