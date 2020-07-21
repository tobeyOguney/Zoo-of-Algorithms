# Boggle Board

You are given a two-dimensional array (matrix) of potentially unequal height and width containing letters; this matrix
represents a boggle board. You are also given a list of words. Write a function that returns an array of all the words
contained in the boggle board. A word is constructed in the boggle board by connecting adjacent (horizontally, vertically,
or diagonally) letters, without using any single letter at a given position more than once; while words can of course have
repeated letters, those repeated letters must come from different positions in the boggle board in order for the word to
be contained in the board. Note that two or more words are allowed to overlap and use the same letters in the boggle
board.


Sample input:
```
[
["t","h","i","s","i","s","a"],
["s","i","m","p","l","e","x"],
["b","x","x","x","x","e","b"],
["x","o","g","g","l","x","o"],
["x","x","x","D","T","r","a"],
["R","E","P","E","A","d","x"],
["x","x","x","x","x","x","x"],
["N","O","T","R","E","-","P"],
["x","x","D","E","T","A","E"],
],

["this","is","not","a","simple","boggle","board","test","REPEATED","NOTRE-PEATED"]
Sample output: ["this","is","a","simple","boggle","board","NOTRE-PEATED"]
```