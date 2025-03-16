## Problem Statement
In a classroom debate, two syllabuses — Syllabus 1 and Syllabus 2 — are being compared to determine which one is more engaging for students. 
Each syllabus contains an equal number of chapters. The syllabus with the higher interest value is selected for teaching.

_Interest Value Calculation_ <br>
The interest value of a syllabus is defined as the sum of the intent values of all its chapters. The interest value of a chapter is determined as follows:

- For a given chapter in one syllabus, count the number of chapters in the other syllabus that have an intrinsic value less than or equal to its own intrinsic value.
- The sum of these counts across all chapters gives the total interest value of the syllabus.

The syllabus with the higher interest value is chosen.

## Input Format

- The first line contains n, the number of chapters in both syllabuses.
- The second line contains n numbers, ai, the intrinsic values for all the chapters in syllabus 1.
- The third line contains n numbers, bi, the intrinsic values for all the chapters in syllabus 2

## Output Format
Your task is to print the highest interest value among both available syllabuses.

## Constraints

- 1 <= n <= 10^5
- 1 <= ai <= 10^9
- 1 <= bi <= 10^9

## Sample Testcase 0

### Testcase Input
1 <br>
2 <br>
4

### Testcase Output
1

### Explanation

- Syllabus 1: [2]
  - Intent value for chapter 2: 0 (since no chapters in Syllabus 2 have intrinsic values ≤ 2).
  - Total interest value of Syllabus 1 = 0.

- Syllabus 2: [4]
  - Intent value for chapter 4: 1 (since one chapter in Syllabus 1 has an intrinsic value ≤ 4).
  - Total interest value of Syllabus 2 = 1.

The highest interest value is 1.

## Sample Testcase 1

### Testcase Input

5 <br>
1 2 6 3 2 <br>
2 4 1 12 2

### Testcase Output
16

### Explanation

Intrinsic values for each syllabus:
- Syllabus 1: [1, 2, 6, 3, 2]
- Syllabus 2: [2, 4, 1, 12, 2]

_Calculating interest values:_

- Syllabus 1:
  - Chapter 1 (1): Count of values in Syllabus 2 ≤ 1 → 1
  - Chapter 2 (2): Count of values in Syllabus 2 ≤ 2 → 3
  - Chapter 3 (6): Count of values in Syllabus 2 ≤ 6 → 4
  - Chapter 4 (3): Count of values in Syllabus 2 ≤ 3 → 3
  - Chapter 5 (2): Count of values in Syllabus 2 ≤ 2 → 3

Total interest value of Syllabus 1 = 1 + 3 + 4 + 3 + 3 = 14

- Syllabus 2:
  - Chapter 1 (2): Count of values in Syllabus 1 ≤ 2 → 3
  - Chapter 2 (4): Count of values in Syllabus 1 ≤ 4 → 4
  - Chapter 3 (1): Count of values in Syllabus 1 ≤ 1 → 1
  - Chapter 4 (12): Count of values in Syllabus 1 ≤ 12 → 5
  - Chapter 5 (2): Count of values in Syllabus 1 ≤ 2 → 4

Total interest value of Syllabus 2 = 3 + 4 + 1 + 5 + 4 = 16

The highest interest value is 16.

## Problem Link

[Click Here](https://unstop.com/courses/unstop-practice-interview-pep/30-days-dsa-bootcamp/day-advanced-searching-37798/coding-question-37801/)
