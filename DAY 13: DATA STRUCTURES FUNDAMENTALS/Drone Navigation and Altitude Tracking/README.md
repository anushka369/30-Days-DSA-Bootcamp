## Problem Statement

In a bustling city, a delivery drone was assigned a special task to navigate through a sequence of `n + 1` points on its route. 
The drone's journey began at point `0`, where its altitude was precisely 0 meters above sea level. <br> <br>
As the drone traveled, it experienced changes in altitude due to urban landscapes, weather conditions, and delivery tasks. 
For every segment between points `i` and `i + 1`, where `0 ≤ i < n`, the change in altitude was represented by an integer array called change, of length `n`. 
The value `change[i]` denoted the net change in altitude between points `i` and `i + 1`. A positive value represented an ascent, 
while a negative value indicated a descent. <br> <br> However, the drone's battery and design imposed a unique constraint: if the altitude at any point along 
the journey became negative, the drone would activate its emergency hover mode, resetting the altitude to `0` meters at that point before continuing its journey.
<br> <br> The drone's mission is to determine the maximum altitude it reached during its journey, considering this unique altitude-resetting mechanism.

## Input Format

- The first line contains an integer `N`, representing the number of elements in the array `change`.
- The second line contains `N` space-separated integers, the elements of the array `change`.

## Output Format
Print a single integer, the maximum altitude the drone reached during its journey.

## Constraints

- 1 <= N <= 10^7
- -10^8 <= change[i] <= 10^8

## Sample Testcase 0

### Testcase Input
5 <br>
-4 2 3 -5 6

### Testcase Output
6

### Explanation

The journey begins at altitude 0.
- After the first segment: Altitude = 0 + (-4) = -4 → resets to 0 due to hover mode.
- After the second segment: Altitude = 0 + 2 = 2.
- After the third segment: Altitude = 2 + 3 = 5.
- After the fourth segment: Altitude = 5 + (-5) = 0 (no reset needed, already 0).
- After the fifth segment: Altitude = 0 + 6 = 6.

The maximum altitude reached is 6.

## Sample Testcase 1

### Testcase Input
6 <br>
3 -2 4 -8 5 2

### Testcase Output
7

### Explanation

The journey begins at altitude 0.
- After the first segment: Altitude = 0 + 3 = 3.
- After the second segment: Altitude = 3 + (−2) = 1.
- After the third segment: Altitude = 1 + 4 = 5.
- After the fourth segment: Altitude = 5 + (−8) = −3 → resets to 0 due to hover mode.
- After the fifth segment: Altitude = 0 + 5 = 5.
- After the sixth segment: Altitude = 5 + 2 = 7.

The maximum altitude reached is 7.

## Problem Link

[Click Here](https://unstop.com/courses/unstop-practice-interview-pep/30-days-dsa-bootcamp/day-data-structures-fundamentals-37811/coding-question-37815)
