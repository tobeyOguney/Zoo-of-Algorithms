# Solves the longest string chain problem


# O(nm) time | O(n+m) space
def kmp_algo(first_string, second_string):
    # Add memo table offset to both strings
    first_string = "*" + first_string
    second_string = "*" + second_string

    # Implement minified memo table
    memo = [
        [True for _ in range(len(first_string))],
        [False for _ in range(len(first_string))]
    ]

    for i in range(1, len(second_string)):     # Loop over rows
        for j in range(1, len(first_string)):  # Loop over columns
            if second_string[i] == first_string[j]:
                memo[1][j] = memo[0][j]
            else:
                memo[1][j] = memo[1][j-1]
        
        # print(memo[1])                    # View minified memo table

        memo[0] = list(memo[1])             # Make room for the next row in the minified memo table

    return memo[-1][-1]

# O((nm)^2) time | O(nm) space
def long_string_chain_kmp(string_list, distance=1):
    # Adjust the list for memo table offset
    string_list.sort(key=len)
    string_list = [""] + string_list

    # Implement minified memo table
    memo = [
        [[[]] for _ in range(len(string_list))] for _ in range(2)
    ]

    for i in range(1, len(string_list)):       # Iterate over rows
        activated = False
        
        for j in range(1, len(string_list)):   # Iterate over columns
            if kmp_algo(string_list[j], string_list[i]):
                if (i == j and not memo[1][j-1][-1]) or \
                (memo[1][j-1][-1] and len(string_list[j]) -  len(memo[1][j-1][-1]) == distance):
                    temp = memo[1][j-1] + [string_list[j]]
                    memo[1][j] = temp if len(temp) > len(memo[0][j]) else memo[0][j]
                    activated = True

                else:
                    memo[1][j] = memo[1][j-1] if activated and len(memo[1][j-1]) >= len(memo[0][j]) else memo[0][j]

            else:
                memo[1][j] = memo[1][j-1] if activated and len(memo[1][j-1]) >= len(memo[0][j]) else memo[0][j]
        
        # print(memo[1]) # View memo table
        
        memo[0] = list(memo[1])     # Creates space for next row in minified memo table

    res =  memo[-1][-1][1:][::-1]

    return res if len(res) > 1 else []


def get_chain(htbl):
    entry_point = max(htbl, key=lambda k: htbl[k][1])
    res = [entry_point]

    while htbl[entry_point][0]:
        res.append(htbl[entry_point][0])
        entry_point = htbl[entry_point][0]
    
    return res

# O(n*m^2) time | O(nm) space
def long_string_chain(string_list):
    string_list.sort(key=len)
    
    htbl = dict()

    for string_ in string_list:
        next_strings = []

        for i in range(len(string_)):
            temp = string_[:i] + string_[i+1:]

            if temp in htbl:
                next_strings.append(temp)

        if next_strings:
            next_string = max(next_strings, key=lambda s: htbl[s][1])
            htbl[string_] = [next_string, htbl[next_string][1] + 1]
        
        else:
            htbl[string_] = ['', 1]
    
    return get_chain(htbl)
    

if __name__ == "__main__":
    res = long_string_chain(
        ["abde", "abc", "abd", "abcde", "ade", "ae", "1abde", "abcdef"]
    )

    assert res == ["abcdef", "abcde", "abde", "ade", "ae"], res

    print("You're all set!")