## Problem Statement

In the enchanted forest of Snoopville, the wise owl known as Orlon is the guardian of the mystical treasure. 
Every year, Orlon holds a challenge to find the worthy adventurer who can solve the riddles of the forest and earn the treasure.
The challenge is simple but requires both wit and knowledge of the forest’s magical rules. 
The adventurer must speak a word aloud within 5 seconds after the bell rings. 
However, only those who meet the conditions of the forest will qualify for the treasure hunt.

To qualify for the next round of the challenge, the word spoken by the adventurer must:
- Contain at least 2 vowels.
- The number of consonants in the word must be a perfect square of a prime number (from the sequence: 2^2, 3^2, 5^2, 7^2, 11^2, 13^2, 17^2, 19^2,.......).
- If the word has no consonants, the adventurer will be disqualified.

As the judge of the challenge, your task is to determine whether each adventurer qualifies for the next stage based on their word.

## Input Format
The only line of input contain a single word consisting of uppercase or lowercase alphabets.

## Output Format
Print "Qualify" if the adventurer qualifies, otherwise print "Disqualify".

## Constraints
1 <= |word| <= 10^5

## Sample Testcase 0

### Testcase Input
Challenge

### Testcase Output
Disqualify

### Explanation

- Vowel(s): A, E, E (3 vowels)
- Consonants: C, H, L, L, N, G (6 consonants)

6 consonants does not meet the required condition (6 is not a perfect square of a prime number).

## Sample Testcase 1

### Testcase Input
BeUnstoppables

### Testcase Output
Qualify

### Explanation

- Vowel(s): E, U, O, A, E (5 vowels)
- Consonants: B, N, S, T, P, P, B, L, S (9 consonants)

9 consonants : 9 is the perfect square of 3.

## Problem Link

[Click Here](https://unstop.com/courses/unstop-practice-interview-pep/30-days-dsa-bootcamp/day-strings-basics-37781/coding-question-37785/)
