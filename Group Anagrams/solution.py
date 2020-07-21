# Solves the group anagrams problem

# What is the strategy to use here?
# O(n) space (hashmap) with sorted string keys
# O(nlg m) time, however this gives O(n^2 lg m) in the worst case

# Is it possible to do better?
# The fact that the output is grouped makes the hash table a natural choice
# Imma go with it

def group_anagrams(lis):
    htbl = dict()

    for s in lis:
        hsh = ''.join(sorted(s))
        htbl.setdefault(hsh, []).append(s)
    
    return list(htbl.values())


if __name__ == "__main__":
    res = group_anagrams(
        ["yo", "act", "flop", "tac", "cat", "oy", "olfp"]
    )

    assert res == [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"]], res

    print("You're all set!")