## Problem Statement
In the city of Unstop, there are `n` citizens known as Unstoppables located at positions `A[i]` along a straight avenue. 
Additionally, there are `m` precious skill spells located at positions `B[i]` scattered along the same avenue.
- Each Unstoppable must collect one skill spell and deliver it to the central museum located at position `p` on the avenue.
- Each Unstoppable moves at a speed of one unit distance per second. 
- If multiple Unstoppables reach a skill spell simultaneously, only one can claim it, and the others must find another skill spell.
- Once a skill spell is taken, it cannot be claimed by another Unstoppable.
  
The goal is to determine the minimum time required for all `n` Unstoppables to deliver their collected skill spells to the museum.

## Input Format

- The first line contains three integers `n`, `m`, and `p`, the number of Unstoppables, the number of skill spells, and the position of the museum, respectively.
- The second line contains `n` space-separated integers `A[i]` the positions of the Unstoppables.
- The third line contains `m` space-separated  integers `B[i]` the positions of the skill spells.
 
## Output Format
Print a single integer the minimum time required for all `n` Unstoppables to deliver their skill spells to the museum.

## Constraints

- 1 <= n, m <= 10^5
- 1 <= A[i], B[i], p <= 10^9

## Sample Testcase 0

### Testcase Input

2 3 5 <br>
1 4 <br>
3 6 8

### Testcase Output
4

### Explanation

- Unstoppable at position 1 goes to skill spell at position 3 and then to the museum at position 5
  <br> Time = |1 - 3| + |3 - 5| = 2 + 2 = 4
- Unstoppable at position 4 goes to skill spell at position 6 and then to the museum at position 5
  <br> Time = |4 - 6| + |6 - 5| = 2 + 1 = 3
- Minimum time is the maximum of these times: max(4, 3) = 4

## Sample Testcase 1

### Testcase Input
3 3 10 <br>
1 5 7 <br>
3 6 8

### Testcase Output
9

### Explanation

- Unstoppable at position 1 goes to skill spell at position 3 and then to the museum at position 10
  <br> Time = |1 - 3| + |3 - 10| = 2 + 7 = 9
- Unstoppable at position 5 goes to skill spell at position 6 and then to the museum at position 10
  <br> Time = |5 - 6| + |6 - 10| = 1 + 4 = 5
- Unstoppable at position 7 goes to skill spell at position 8 and then to the museum at position 10
  <br> Time = |7 - 8| + |8 - 10| = 1 + 2 = 3
- Minimum time is the maximum of these times: max(9, 5, 3) = 9

## Problem Link

[Click Here](https://unstop.com/courses/unstop-practice-interview-pep/30-days-dsa-bootcamp/day-mixed-problems-37804/coding-question-37809)
