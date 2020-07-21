# Apartment Hunting

You're looking to move into a new apartment, and you're given a list of blocks where each block contains an apartment that you could
move into. In order to pick your apartment, you want to optimize its location. You also have a list of requirements: a list of buildings that
are important to you. For instance, you might value having a school and a gym near your apartment. The list of blocks that you have
contains information at every block about all of the buildings that are present and absent at the block in question. For instance, for every
block, you might know whether a school, a pool, an ofce, and a gym are present or not. In order to optimize your life, you want to
minimize the farthest distance you'd have to walk from your apartment to reach all of your required buildings. Write a function that
takes in a list of blocks and a list of your required buildings and that returns the location (the index) of the block that is most optimal for
you.

Sample input:
```
[
{
"gym": False,
"school": True,
"store": False,
},
{
"gym": True,
"school": False,
"store": False,
},
{
"gym": True,
"school": True,
"store": False,
},
{
"gym": False,
"school": True,
"store": False,
},
{
"gym": False,
"school": True,
"store": True,
},
],
["gym","school","store"]
```

Sample output:
```
3 (at index 3, the farthest you would have to walk to reach a gym, a school, or a store, is 1 block; at any other index, you
would have to walk farther)
```
