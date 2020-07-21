# Multi String Search

Write a function that takes in a big string and an array of small strings, all of which are smaller
in length than the big string. The function should return an array of booleans, where each boolean
represents whether the small string at that index in the array of small strings is contained in the big string.

Note that you can't use language-built-in string-matching methods.

Sample Input: `"this is a big string", ["this", "yo", "is", "a", "bigger", "string", "kappa"]`

Sample Output: `[true, false, true, true, false, true, false]`