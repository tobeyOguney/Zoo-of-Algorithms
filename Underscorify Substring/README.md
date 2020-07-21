# Underscorify Substring


Write a function that takes in two strings: a main string and a potential substring of the main string. The function should return a version of the main string with
every instance of the substring in it wrapped between underscores. If two instances of the substring in the main string overlap each other or sit side by side, the
underscores relevant to these two substrings should only appear on the far left of the left substring and on the far right of the right substring. If the main string
does not contain the other string at all, return the main string intact.

Sample input:
```
"testthis is a testtest to see if testestest it works","test"
```

Sample output:
```
"_test_this is a _testtest_ to see if _testestest_ it works"
```