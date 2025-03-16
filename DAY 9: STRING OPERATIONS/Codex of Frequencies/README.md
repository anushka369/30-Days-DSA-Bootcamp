## Problem Statement
In the ancient village of Aeloria, there was a mystical book known as the Codex of Frequencies, said to contain powerful knowledge hidden 
within the frequencies of letters. These letters had unique magical properties, with odd frequencies being especially potent. 
Elara, a young and talented apprentice, was tasked with deciphering the book’s secrets. <br>

The key to unlocking the book's power lay in the odd frequencies of the letters. Elara needed to analyze the frequencies and apply a set of rules to determine their magical significance:
- If exactly three letters had odd frequencies, she would calculate the product of those frequencies to reveal a hidden spell.
- If there were more than three odd frequencies, she would select the three largest ones and find their product for a stronger magic.
- If there were fewer than three odd frequencies, Elara had to identify the smallest odd frequency, or return -1 if there were no odd frequencies at all.

As Elara carefully studied the letters, she realized the importance of sorting the frequencies in descending order. 
In case of a tie in frequency, she would need to break it by considering the alphabetical order of the letters.

## Input Format
The first line of input contains a single string str consisting of lowercase English letters.

## Output Format

- If exactly three characters have odd frequencies, print each character and its frequency (sorted by frequency and then alphabetically), followed by their product.
- If more than three characters have odd frequencies, print the three largest odd frequencies (sorted by frequency and then alphabetically), followed by their product.
- If fewer than three odd frequencies exist, print the smallest odd frequency, or -1 if none exist.

## Constraints
2 <= |str| <= 10^8

## Sample Testcase 0

### Testcase Input
aabcccddd

### Testcase Output
c 3 <br>
d 3 <br>
b 1 <br>
9

### Explanation

The string aabcccddd has odd-frequency characters: b: 1, c: 3, d: 3. <br>
After sorting by descending frequency, the top 3 are:
- c 3 
- d 3 
- b 1

Their product is 3 × 3 × 1 = 9.

## Sample Testcase 1

### Testcase Input
mmoppqrr

### Testcase Output
o 1

### Explanation
The string mmoppqrr has odd-frequency characters: o: 1 and q: 1. <br>
Since there are fewer than 3 odd frequencies, the lexicographically smallest character with the smallest odd frequency is printed.

## Problem Link

[Click Here](https://unstop.com/courses/unstop-practice-interview-pep/30-days-dsa-bootcamp/day-string-operations-37787/coding-question-37790/)
