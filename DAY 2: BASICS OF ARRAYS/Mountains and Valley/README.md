## Problem Statement

Given a linked list, determine if it exhibits a continuous mountain and valley pattern. 
A continuous mountain and valley pattern is characterized by a sequence of nodes where the values consistently alternate between increasing and decreasing.
<br> Note: if only one node is present, then return 1.

 ## Input Format
The first line contains an integer 'n' representing the number of nodes in the linked list. <br>
The second line contains 'n' space-separated integers representing the values of the nodes in the linked list.

## Output Format

- '1' indicates that the linked list follows a continuous mountain and valley pattern.
- '0' indicates the linked list does not follow the continuous mountain and valley pattern.

## Constraints

- 1 <= n <= 4 * 10^3
- 0 <= elements of linked list <= 10^4

## Sample Testcase 0

- Testcase Input: <br>
  5 <br>
  1 2 3 2 1
  
- Testcase Output : 0

- Explanation: 1 -> 2 -> 3 -> 2 -> 1 <br>
  As 1 to 3 is increasing, that means values consistently do not alternate between increasing and decreasing.
  <br> So the answer is 0.

## Sample Testcase 1

- Testcase Input: <br>
  5 <br>
  1 2 1 2 1

- Testcase Output : 1

- Explanation : 1 -> 2 -> 1 -> 2 -> 1 <br>
  As values consistently alternate between increasing and decreasing.
  <br> So the answer is 1.

## Link to the problem

[Click here](https://unstop.com/courses/unstop-practice-interview-pep/30-days-dsa-bootcamp/day-basics-of-arrays-37720/coding-question-37722/)
