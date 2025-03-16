## Problem Statement
In a distant galaxy, a young inventor named Leo created a robot called "Trace" to help him find hidden treasures. 
These treasures were marked on ancient maps stored as long strings of mysterious text. 
To locate a treasure, Trace needed to find a specific clue called the Key, made up of a unique combination of characters.
The maps were massive and full of random symbols, making Trace’s task difficult. 
The Key could appear in any part of the map, but its characters might be jumbled. 
Trace’s job was to find the shortest section(substring) of the map that included all the characters of the Key, no matter the order. 
If no such substring exists, Trace should return -1.

## Input Format

- The first line contains a string S representing the map.
- The second line contains a string T representing the Key.

## Output Format
- Output the length of the shortest substring of s that contains all the characters of t in any order.
- If no such substring exists, output -1.

## Constraints

- Each character of S and T is a printable ASCII character.
- 1 ≤ |S| ≤ |T| ≤ 10^5

## Sample Testcase 0

### Testcase Input
warrmioruhk <br>
warrior

### Testcase Output
8

### Explanation
The shortest substring of S that contains all the characters of T is "warrmior", which has length 8.

## Sample Testcase 1

### Testcase Input
Thunder <br>
King

### Testcase Output
-1

### Explanation
There is no substring of S that contains all the characters of T.

## Problem Link

[Click Here](https://unstop.com/courses/unstop-practice-interview-pep/30-days-dsa-bootcamp/day-string-operations-37787/coding-question-37789/)
