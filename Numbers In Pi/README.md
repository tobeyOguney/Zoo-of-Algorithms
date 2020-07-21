# Numbers In Pi

Given a string representation of the first n digits of Pi and a list of your favorite numbers
(all positive integers in string format),

write a function that returns the smallest number of spaces that need to be added
to the n digits of Pi such that all resulting numbers are found in the list of favorite numbers.
If no number of spaces to be added exists such that all resulting numbers are found in the list of
favorite numbers, the function should return -1.

Sample input:
```
"3141592653589793238462643383279",
["314159265358979323846", "26433", "8", "3279", "314159265", "35897932384626433832", "79"]
```

Sample output: `2 ("314159265 | 35897932384626433832 | 79")`