# Implementation of the Knuth-Morris-Pratt Algorithm


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


if __name__ == "__main__":
    res = kmp_algo("aefoaefcdaefcdaed", "aefcdaed")

    assert res == True, "Not quite there yet..."

    print("You're all set!")