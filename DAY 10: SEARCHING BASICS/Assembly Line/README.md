## Problem Statement

In an assembly line at St. Mary School, N students stand in ascending order of their heights. 
Nidhi Sharma, a teacher, has k queries where she asks about the height H of a particular student. 
The task is to determine the position (0-based index) of the student in the line if they are present. 
If the student is absent, the task is to find the correct position where that student should be placed to maintain the ascending order.

## Input Format

- The first line contains the integer N denoting the total no. of students.
- The second line contains N space-separated integers representing the height of students standing in a line.
- The third line contains an integer k denoting the number of queries of the teacher.
- Next k lines contain a single integer on each line denoting the height of the student H that is enquired.

## Output Format
For each query, output the proper position (0-based index) of the student in a new line.

## Constraints

- 1 <= k <= 10^3
- 1 <= N <= 10^8
- 1 <= hi <= 10^4
- 1 <= H <= 10^4

## Sample Testcase 0

### Testcase Input

5 <br>
12 34 45 89 110 <br>
5 <br>
23 <br>
45 <br>
11 <br>
90 <br>
150

### Testcase Output

1 <br>
2 <br>
0 <br>
4 <br>
5

### Explanation

- 23: The height 23 is not present in the list, but it should be placed between 12 and 34 to maintain ascending order. So, its correct position (0-based index) is 1.
- 45: The height 45 is present in the list at position 2 (0-based index). So the correct position (0-based index) is 2.
- 11: The height 11 is not present, but it shuld be placed before 12. So, its correct position (0-based index) is 0.
- 90: The height 90 is not present, but it should be placed after 89 and before 110. So, its correct position (0-based index) is 4.
- 150: The height 150 is not present but it would be placed after 110. So, its correct position (0-based index) is 5.

## Sample Testcase 1

### Testcase Input

4 <br>
1 3 5 6 <br>
2 <br>
5 <br>
7

### Testcase Output

2 <br>
4

### Explanation

- The first query asks for the position of the student with a height 5.
  - Since 5 is present in the list at position 2 (0-based index).
- The second query asks for the position of the student with height 7.
  - Since 7 is not present, but it would be placed after 6 to maintain ascending order, its correct position (0-based index) is 4.

## Problem Link

[Click Here](https://unstop.com/courses/unstop-practice-interview-pep/30-days-dsa-bootcamp/day-searching-basics-37792/coding-question-37797/)
