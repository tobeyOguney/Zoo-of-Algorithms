# Longest String Chain

Given a list of strings, write a function that returns the longest string chain that can be
built from those strings.

A string chain is defined as follows:

let string A be a string in the initial array;

if removing any single character from string A yields a new string B that is contained in the initial array of strings, then strings A and B form a string chain of length 2.

Similarly, if removing any single character from string B yields a new string C that is
contained in the initial array of strings, then strings A, B, and C form a string chain of length 3.

The function should return the string chain in descending order (i.e., from the longest string to the shortest one).

Note that string chains of length 1 do not exist;

if the list of strings does not contain any string
chain formed by 2 or more strings, the function should return an empty list.

**Sample input**: `["abde", "abc", "abd", "abcde", "ade", "ae", "1abde", "abcdef"]`

**Sample output**: `["abcdef", "abcde", "abde", "ade", "ae"]`
