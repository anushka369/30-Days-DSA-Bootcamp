## Problem Statement

In Unstop's  magical kingdom, a messenger must navigate a treacherous enchanted grid to deliver an urgent message to the royal palace. 
The grid is an ancient map, where each cell contains a rune that dictates the direction of movement: <br>
- a: Move 1 unit right
- b: Move 1 unit left
- c: Move 1 unit down
- d: Move 1 unit up.

The messenger starts at the top-left corner of the map (0, 0) and must reach the palace at the bottom-right corner (m−1, n−1). 
However, the map's runes have been corrupted over time, and not all paths lead to the destination.
The messenger can use his magical power  to alter any rune, but each alteration consumes precious mana, costing 1 unit per change. 
The messenger must find the minimum mana required to adjust the map so that at least one path leads to the palace.
Will the messenger succeed in delivering the message in time? Your task is to determine the minimum mana required to ensure they reach their destination!

## Input Format

- The first line contains two space separated integers M and N, representing the rows and columns of the grid.
- The next N line each containing M values, a, b c, d.

## Output Format
Print an integer representing the minimum cost (mana) required to ensure there is at least one valid path from the top-left corner to the bottom-right corner.

## Constraints
1 <= M, N <= 10^3

## Sample Testcase 0

### Testcase Input

3 3 <br>
a a b <br>
c a d <br>
b b c

### Testcase Output
2

### Explanation

Starting from the top-left cell (0, 0): <br>
1. Cell (0, 0): a (right), no cost to move to (0, 1).
2. Cell (0, 1): a (right), no cost to move to (0, 2).
3. Cell (0, 2): b (left), modify to move down to (1, 2) at a cost of 1.
4. Cell (1, 2): d (up), modify to move down to (2, 2) at a cost of 1.
5. Cell (2, 2): Destination reached.

## Sample Testcase 1

### Testcase Input

4 4 <br>
a b c d <br>
b b a c <br>
c c d b <br>
d a a a

### Testcase Output
2

### Explanation

Starting from the top-left cell (0, 0): <br>
1. Cell (0, 0): a (right), no cost to move to (0, 1).
2. Cell (0, 1): b (left), modify to move down to (1, 1) at a cost of 1.
3. Cell (1, 1): b (left), modify to move down to (2, 1) at a cost of 1.
4. Cell (2, 1): c (down), no cost to move to (3, 1).
5. Cell (3, 1): a (right), no cost to move to (3, 2).
6. Cell (3, 2): a (right), no cost to move to (3, 3).
7. Cell (3, 3): Destination reached.

## Problem Link

[Click Here](https://unstop.com/courses/unstop-practice-interview-pep/30-days-dsa-bootcamp/day-mixed-problems-37748/coding-question-37827/)
