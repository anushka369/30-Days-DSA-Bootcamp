## Problem Statement
Pavel is given a room with N seats and N students. 
Each seat's position is represented by the array seats of length N, where seats[i] indicates the position of the ith seat.
Similarly, the positions of the students are given in an array students of length N, where students[j] represents the position of the jth student.
Pavel is allowed to move each student by one position to the left or right any number of time. 
The goal is to find the minimum number of moves required to shift the students to seats in such a way that no two students are seated together.

## Input Format

- The first line of the input contains an integer N representing the number of seats and students.
- The second line contains N space-separated integers representing the position of ith seats.
- The third line contains N space-separated integers representing the position of ith students.

## Output Format
Print the minimum number of moves required to move each student to a seat.

## Constraints

- N == seats.length == students.length
- 1 <= N <= 100
- 1 <= seats[i], students[j] <= 100

## Sample Testcase 0

### Testcase Input

4 <br>
2 4 6 8 <br>
2 4 6 8

### Testcase Output
0

### Explanation

Similar to the previous case, the initial arrangement already satisfies the condition. No moves are necessary.

## Sample Testcase 1

### Testcase Input

5 <br>
1 3 5 7 9 <br>
2 4 6 8 10

### Testcase Output
5

### Explanation
The students start at positions [2, 4, 6, 8, 10], but they need to be moved to [1, 3, 5, 7, 9] to ensure that no two students are adjacent.

The minimum moves required:

- Move student from 2 → 1 (1 move)
- Move student from 4 → 3 (1 move)
- Move student from 6 → 5 (1 move)
- Move student from 8 → 7 (1 move)
- Move student from 10 → 9 (1 move)
  
Total moves = 5

## Problem Link

[Click Here](https://unstop.com/courses/unstop-practice-interview-pep/30-days-dsa-bootcamp/day-arrays-operations-37726/coding-question-37729/)
