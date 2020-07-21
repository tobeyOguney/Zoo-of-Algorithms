# Branch Sums

Given a binary tree **bt**, generate a list of sums obtained by summing the nodes for each root-to-leaf path in **bt**.

### Example:

```
           6
       /      \
     3          5
   /   \          \
  2     5          4  
      /   \
     7     4
  There are 4 leaves, hence 4 root to leaf paths:
   Path                    Number
  6->3->2                   11
  6->3->5->7                21
  6->3->5->4                18
  6->5>4                    15

  Result = [11, 21, 18, 15] 
```