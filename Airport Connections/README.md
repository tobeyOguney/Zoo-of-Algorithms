## Airport Connections

#### Problem Statement

You are given a list of airports (three-letter codes like 'JFK'), a list of routes (one-way ights from one airport to another like ['JFK', 'SFO']), and
a starting airport. Write a function that returns the minimum number of airport connections (one-way ights) that need to be added in order
for someone to be able to reach any airport in the list, starting at the starting airport. Note that the connections don't have to be direct; it's
okay if an airport can only be reached from the starting airport by stopping at other airports rst.

Sample input:
```
[
"BGI",
"CDG",
"DEL",
"DOH",
"DSM",
"EWR",
"EYW",
"HND",
"ICN",
"JFK",
"LGA",
"LHR",
"ORD",
"SAN",
"SFO",
"SIN",
"TLV",
"BUD",
],
[
["DSM","ORD"],
["ORD","BGI"],
["BGI","LGA"],
["SIN","CDG"],
["CDG","SIN"],
["CDG","BUD"],
["DEL","DOH"],
["DEL","CDG"],
["TLV","DEL"],
["EWR","HND"],
["HND","ICN"],
["HND","JFK"]
["ICN","JFK"],
["JFK","LGA"],
["EYW","LHR"],
["LHR","SFO"],
["SFO","SAN"],
["SFO","DSM"],
["SAN","EYW"],
],
"LGA"
```

Sample output: `3`