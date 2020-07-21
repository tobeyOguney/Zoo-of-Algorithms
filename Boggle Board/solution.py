# Solves the boggle board problem


class Trie:
    def __init__(self):
        self.root = dict()
        self.end_symbol = "*"
    
    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = dict()
                
            current = current[letter]
        
        current[self.end_symbol] = word


def get_suffix_trie(words):
    trie = Trie()

    for word in words:
        trie.add(word)

    return trie

def get_next_idxs(i, j, max_i, max_j):
    neighbours = []

    if i > 0 and j > 0:
        neighbours.append([i-1, j-1])
    
    if i > 0 and j < max_j - 1:
        neighbours.append([i-1, j+1])
    
    if i < max_i - 1 and j < max_j - 1:
        neighbours.append([i+1, j+1])
    
    if i < max_i - 1 and j > 0:
        neighbours.append([i+1, j-1])
    
    if i > 0:
        neighbours.append([i-1, j])
    
    if i < max_i - 1:
        neighbours.append([i+1, j])
    
    if j > 0:
        neighbours.append([i, j-1])
    
    if j < max_j - 1:
        neighbours.append([i, j+1])
    
    return neighbours

def explore(i, j, board, root, res, visited):
    if (i, j) in visited:
        return
    
    if "*" in root:
        res.add(root["*"])
    
    visited.add((i, j))

    next_idxs = get_next_idxs(i, j, len(board), len(board[0]))

    for idxs in next_idxs:
        new_root = root.get(board[idxs[0]][idxs[1]], {})

        if new_root:
            explore(idxs[0], idxs[1], board, new_root, res, visited)
    
    visited.difference_update({(i, j)})

# I figured that using an iterative solution here will be state management hell!
# With recursion, we shall forge ahead!!!

# O(n^3) time | O(n^2) space
def boggle_board(board, words):
    sfx_trie = get_suffix_trie(words)
    res = set()
    visited = set()

    for i in range(len(board)):         # Iterate over rows
        for j in range(len(board[0])):  # Iterate over columns
            explore(i, j, board, sfx_trie.root, res, visited)
            
    return res
                

if __name__ == "__main__":
    res = boggle_board(
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
    )

    assert set(res) == set(["this","is","a","simple","boggle","board","NOTRE-PEATED"]), res

    print("You're all set!")