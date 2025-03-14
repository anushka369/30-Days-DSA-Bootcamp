## Problem Statement

In a futuristic space station, a garden of genetically engineered plants generates energy pods, represented as an array E of size N,
where E[i] is the number of energy pods produced by the i-th plant. Commander Zeta must divide the garden into three continuous zones: 
Alpha, Beta and Gamma where the zone size of alpha must be same as the zone size of gamma.
Alpha and Gamma for the Energy Council, and Beta for the Defense Alliance. Since Zone Beta is inefficient and wastes energy, 
Zeta decides to ensure its energy is always less than the combined energy of Zones Alpha and Gamma.
Determine the total number of ways this division can be accomplished while adhering to this condition.

## Input Format

- The first line contains an integer N representing the number of plants.
- The second line contains N space separated integers, where the i-th integer represents the energy pods produced by the i-th plant.

## Output Format
Print a single integer representing the total number of ways to divide the garden into the three zones such 
that the sum of energy pods in Alpha and Gamma combined is greater than the energy pods in Beta.

## Constraints

- 1 <= N <= 10^5
- 1 <= E[i] <= 10^5

## Sample Testcase 0

### Testcase Input

4 <br>
3 3 3 3

### Testcase Output
0

### Explanation
For the array [3, 3, 3, 3], there are no valid divisions possible.

## Sample Testcase 1

### Testcase Input

5 <br>
1 2 3 4 5

### Testcase Output
1

### Explanation
For the array [1, 2, 3, 4, 5], there will be only one possible division.
<br> Alpha: [1, 2], Beta: [3], Gamma: [4, 5] → (3 + 9 > 3)

## Problem Link

[Click Here](https://unstop.com/courses/unstop-practice-interview-pep/30-days-dsa-bootcamp/day-subarrays-37731/coding-question-37734/)
