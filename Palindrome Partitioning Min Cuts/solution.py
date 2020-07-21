# Solves the palindrome partitioning min cuts problem

# Consider all the prefixes
# If a prefix is a palindrome, consider the corresponding suffix as a prefix
# These recursive calls should share a memo

# O(n^3) time | O(n^2) space
def palind_min_cuts(string_, memo={'': -1}):
    if not string_:
        return
    
    if string_ in memo:
        return

    for i in range(len(string_)):
        prefix = string_[:i+1]
        if prefix == prefix[::-1]:
            suffix = string_[i+1:]

            _ = palind_min_cuts(suffix)

            memo[string_] = min(memo.get(string_, float("inf")), 1 + memo[suffix])
    
    return memo.get(string_, -1)

# O(n^2) time | O(n^2) space
def get_palind_memo(string_):
    # Implement memo table
    memo = [[False for _ in range(len(string_))] for _ in range(len(string_))]

    for i in range(len(string_)):           # Loop over rows
        for j in range(len(string_)):       # Loop over columns
            if j >= i:
                memo[i][j] = string_[i] == string_[j]
    
    # print(memo)   # Verify memo table

    return memo

# O(n^2) time | O(n^2) space
def dyn_palind_min_cuts(string_):
    is_palind = get_palind_memo(string_)

    # Implement memo list
    memo = [i for i in range(len(string_))]

    for i in range(len(memo)):
        if is_palind[0][i]:
            memo[i] = 0
        
        else:
            memo[i] = memo[i-1] + 1
            for j in range(1, i):
                if is_palind[j][i]:
                    memo[i] = min(memo[i], memo[j-1]+1)
    
    # print(memo)   # Verify memo list

    return memo[-1]


if __name__ == "__main__":
    res = dyn_palind_min_cuts("noonabbad")

    assert res == 2, res

    print("You're all set!")