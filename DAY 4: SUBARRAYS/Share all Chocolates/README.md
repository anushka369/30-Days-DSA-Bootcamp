## Problem Statement

Alice’s mom bought `N` bags of chocolates numbered from 1 to N. The ith bag (`1 <= i <= N`) has `Ai` chocolates.
Alice wants to share some of the chocolate bags with Bob such that both of them get an equal number of chocolates, 
but she is not able to divide them in such a way. Now, she wonders if it is even possible to do so.
Help Alice find out if the bags can be divided between her and Bob such that both of them get an equal number of chocolates.
Remember you cannot divide the chocolate inside the bags. 

## Input Format

- The first line of the input contains a single integer N denoting the number of bags that Alice’s mom bought.
- The second line contains N space-separated integers `A1, A2, …, An` – the number of chocolates in each bag.

## Output Format
If it is possible to divided the chocolate bags in two parts with equal chocolates, print “YES” (without quotes). Otherwise, print “NO” (without quotes).

## Constraints

- 1 <= N <= 5 * 10^2
- 1 <= Ai <= 10^2

## Sample Testcase 0

### Testcase Input

4 <br>
1 2 3 3

### Testcase Output
NO

### Explanation
It is not possible to divid the chocolate bags in two parts with equal chocolates.

## Sample Testcase 1

### Testcase Input

4 <br>  
1 2 3 4

### Testcase Output
YES

### Explanation
The total number of chocolates is 1 + 2 + 3 + 4 = 10 <br>
Since 10 is even, it's possible to divide the chocolates equally. <br>
One possible division is:
- Alice: 1, 4 (total = 5).
- Bob: 2, 3 (total = 5).

## Problem Link

[Click Here](https://unstop.com/courses/unstop-practice-interview-pep/30-days-dsa-bootcamp/day-subarrays-37731/coding-question-37735/)
