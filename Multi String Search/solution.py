# Solves the multistring search problem

class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = None
    
    # O(s) time | O(s) space
    def insert(self, string_):
        temp = self.root

        for i in range(len(string_)):
            temp[string_[i]] = {self.end_symbol: string_} if i == len(string_) - 1 else {}
            temp = temp[string_[i]]


# O(bs + ns) time | O(ns) space
def multi_string_search(big_string, small_string_list):
    # Build trie using small strings in O(ns) time | O(ns) space
    trie = Trie()
    for small_string in small_string_list:
        trie.insert(small_string)

    results = {small_string: False for small_string in small_string_list}

    for i in range(len(big_string)):        # O(bs) time
        j = i
        sub_trie_root = trie.root

        while None not in sub_trie_root and big_string[j] in sub_trie_root:
            sub_trie_root = sub_trie_root[big_string[j]]
            j += 1
        
        if None in sub_trie_root:
            results[sub_trie_root[None]] = True
    
    return [results[small_string] for small_string in small_string_list]
                




if __name__ == "__main__":
    res = multi_string_search(
        "this is a big string",
        ["this", "yo", "is", "a", "bigger", "string", "kappa"]
    )

    assert res == [True, False, True, True, False, True, False], res

    print("You're all set!")