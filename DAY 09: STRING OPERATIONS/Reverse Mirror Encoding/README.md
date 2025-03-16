## Problem Statement

Ram and Shyam have devised a new encoding scheme called "Reverse Mirror Encoding." In this system:

- For letters 'a' to 'n', the code is their reverse position in the first half of the alphabet.
  <br> Example: 'a' → n, 'b' → m, ..., 'n' → a.

- For letters 'o' to 'z', the code is their reverse position in the second half of the alphabet followed by a #.
  <br> Example: 'o#' → z, 'p#' → y, ..., y# → p, 'z#' → o. <br>

Given a coded message S, determine the original decoded message Ram sent to Shyam.

## Input Format
The first and only line of input contains a single string S, representing the encoded message.
 
## Output Format
Print a single string, representing the decoded message.

## Constraints
2 <= |S| <= 10^3

## Sample Testcase 0

### Testcase Input
u#jlg

### Testcase Output
tech

### Explanation

'u#' → 't' <br>
'j' → 'e' <br>
'l' → 'c' <br>
'g' → 'h' <br>
Decoded message: "tech"

## Sample Testcase 1

### Testcase Input
mjt#av#u#z#y#y#nmcj

### Testcase Output
beunstoppable

### Explanation
'm' → 'b' <br>
'j' → 'e' <br>
't#' → 'u' <br>
'a' → 'n' <br>
'v#' → 's' <br>
'u#' → 't' <br>
'z#' → 'o' <br>
'y#' → 'p' <br>
'y#' → 'p' <br>
'n' → 'a' <br>
'm' → 'b' <br>
'c' → 'l' <br>
'j' → 'e' <br>
Decoded message: "beunstoppable"

## Problem Link

[Click Here](https://unstop.com/courses/unstop-practice-interview-pep/30-days-dsa-bootcamp/day-string-operations-37787/coding-question-37788/)
