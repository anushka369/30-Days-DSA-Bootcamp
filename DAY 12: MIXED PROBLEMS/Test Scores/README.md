## Problem Statement

The exam scores for a class of N students have been released. 
The marks obtained by each student are stored in an array of `scores[]`, where `scores[i]` represent the marks of the `i`-th student.
<br> <br> As the class monitor, Ram is tasked with answering queries from the teacher. 
The teacher will ask `Q` queries, and for each query, Ram needs to determine how many students have scored at least `X` marks.
<br> <br> Your objective is to help Ram by finding the number of students who have scored at least `X` marks for each query.

## Input Format

- The first line contains two positive integers `N`, and `Q`, denoting the number of students and the number of queries, respectively.
- This is followed by a line containing `N` integers, separated by space giving the scores of each student.
- Then, `Q` lines follow where the ith line contains a single integer `X`.

## Output Format
For each query, print a single integer representing the number of students who scored at least `X` marks.

## Constraints

- 1 <= N, Q <= 2 * 10^5
- 1 <= X <= 10^9
- 1 <= scores[i] <= 10^9

## Sample Testcase 0

### Testcase Input
5 2 <br>
1 4 12 3 9
<br> 2 <br>
15

### Testcase Output
4 <br>
0

### Explanation

There are 5 students with scores [1, 4, 12, 3, 9].
- The first query asks for the number of students who scored at least 2 marks. <br>
  The students with scores [4, 12, 3, 9] meet this criterion, resulting in 4 students.
- The second query asks for the number of students who scored at least 15 marks. <br>
  No student meets this criterion, resulting in 0 students.

Therefore, the outputs are 4 and 0 respectively.

## Sample Testcase 1

### Testcase Input
4 1 <br>
2 3 1 4
<br> 3

### Testcase Output
2

### Explanation

There are 4 students with scores [2, 3, 1, 4].
- The query asks for the number of students who scored at least 3 marks.
  <br> The students with scores of 3 and 4 meet this criterion.

Therefore, the output is 2.

## Problem Link

[Click Here](https://unstop.com/courses/unstop-practice-interview-pep/30-days-dsa-bootcamp/day-mixed-problems-37804/coding-question-37810)
