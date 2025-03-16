## Problem Statement

In a forest grid, there is a treasure chest guarded by a beast. A hero must collect keys scattered across the forest to unlock the chest. 
The task is to determine whether the hero can unlock the treasure chest and, if so, the shortest path to do so.
The hero can only reach the chest if they collect all keys first. Obstacles in the forest prevent movement. <br>

_Grid Symbols:_

- 'H': Represents the hero's starting position.
- 'C': Represents the treasure chest's position.
- 'K': Represents a key that must be collected.
- 'O': Represents an obstacle that blocks movement.
- 'P': Represents a path the hero can move on.

_Rules:_

1. The hero must collect all the keys ('K') before they can reach the treasure chest ('C').
2. The hero can move in four directions: up, down, left, and right.
3. If it's not possible to collect all keys or reach the chest, return "Impossible".
4. If it is possible to unlock the chest, return the minimum number of steps/length of shortest path required for the hero to collect all keys and reach the chest.

_Note:_ Once we reach 'C' we can't move further.

## Input Format

- The first line of input contains two space separated integer N and M denoting the dimensions of the grid.
- The next N line each containing M space separated characters representing a 2D array of size NxM where each cell contains one of the following symbols:
  - 'H': Hero's starting position (appears exactly once).
  - 'C': Treasure chest (appears exactly once).
  - 'K': Key(s) to be collected (at least one 'K' is guaranteed).
  - 'O': Obstacle that blocks movement.
  - 'P': Path the hero can move on.

## Output Format

- If the hero can collect all keys and reach the chest, output a single integer denoting the minimum number of steps/length of shortest path required.
- If it is not possible to collect all keys and reach the chest, output "Impossible".

## Constraints

- 1 ≤ N, M ≤ 20
- 1 ≤ N*M ≤ 40

## Sample Testcase 0

### Testcase Input

4 4 <br>
H P K O <br>
O P O P <br>
P K C P <br>
O O P O

### Testcase Output
6

### Explanation

H -> P -> K : 2 steps <br>
backtrack to P : 1 step <br>
P -> P -> K -> C : 3 steps <br>
Total 6 steps.

## Sample Testcase 1

### Testcase Input

3 3 <br>
P P P <br>
O C K <br>
H P O

### Testcase Output
Impossible

### Explanation

The hero must not cross the chest (C) in order to collect the key, so even if a direct path to the chest exists, the hero cannot collect the key, making the task impossible.

## Problem Link

[Click Here](https://unstop.com/courses/unstop-practice-interview-pep/30-days-dsa-bootcamp/day-mixed-problems-37748/coding-question-37828/)
