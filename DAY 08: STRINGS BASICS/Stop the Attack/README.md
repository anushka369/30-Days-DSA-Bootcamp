## Problem Statement

You are an agent, to stop an attack you have to decipher a piece of encrypted code.
The encrypted code contains two lines each containing a sequence of characters. 
You know that to decipher the code you have to merge the two lines by adding characters in alternating sequence. 
Finally, if one sequence is longer than the other append it to the end.
Help the agent decrypt the code as soon as possible. 

## Input Format

- The first line of the input contains an integer n  — the size of the first sequence.
- The second line of the input contains the first sequence.
- The third line of the input contains an integer m  — the size of the second sequence.
- The fourth line of the input contains the second sequence.

## Output Format
Print the decoded sequence of characters. 

## Constraints

- 1 <= sequence1.length, sequence2.length <= 100
- sequence1 and sequence2 consist of lowercase English letters.

## Sample Testcase 0

### Testcase Input

5 <br>
bmatc <br>
5 <br>
obtak

### Testcase Output
bombattack

### Explanation

Adding each character in the sequence: From 1st string (0th Character) - From 2nd string (0th Character) - From 1st string (1st Character) - From 2nd String (1st Character) - From 1st string .....
<br> b - o - m - b - a - t - t - a - c - k. We get the string as "bombattack".

## Sample Testcase 1

### Testcase Input

4 <br>
ctho <br>
5 <br>
acfur

### Testcase Output
catchfour

### Explanation

Adding each character in the sequence: From 1st string (0th Character) - From 2nd string (0th Character) - From 1st string (1st Character) - From 2nd string (1st Character) - From 1st string .....
<br> c - a - t - c - h - f - o - u - r (remaining characters). We get the string as "catchfour".

## Problem Link
[Click Here](https://unstop.com/courses/unstop-practice-interview-pep/30-days-dsa-bootcamp/day-strings-basics-37781/coding-question-37786/)
