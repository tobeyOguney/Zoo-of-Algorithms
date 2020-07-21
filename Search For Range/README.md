# Search For Range

Write a function that takes in a sorted array of integers as well as a target integer. The function should
use a variation of the Binary Search algorithm to find a range of indices in between which the target number
is contained in the array and should return this range in the form of an array.

The first number in the output array should represent the first index at which the target number is located,
while the second number should represent the last index at which the target number is located.
The function should return [-1, -1] if the integer isn't contained in the array.

Sample Input:
```
[0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45
```
Sample Output:
```
[4, 9]
```