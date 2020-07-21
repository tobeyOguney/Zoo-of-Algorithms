# Implements the Levenshtein distance algorithm

# O(nm) time | O(n+m) space
def lev_distance_algo(first_string, second_string):
    # Adjust both strings for memo table offset
    first_string = "*" + first_string
    second_string = "*" + second_string

    # Implement minified memo table
    memo = [
        [i for i in range(len(second_string))],
        [0 for _ in range(len(second_string))]
    ]

    for i in range(1, len(first_string)):
        memo[1][0] = range(len(second_string))[i]   # Corrrectly update first row element in memo table

        for j in range(1, len(second_string)):
            if second_string[j] == first_string[i]: # Coincidence check
                memo[1][j] = memo[0][j-1]

            else:
                memo[1][j] = min(memo[1][j-1], memo[0][j-1], memo[0][j]) + 1
        
        # print(memo[1])      # View memo table

        memo[0] = list(memo[1])   # Create space for the next row in minified memo table

    return memo[-1][-1]

if __name__ == "__main__":
    res = lev_distance_algo("abc", "yabd")

    assert res == 2, "Not quite there yet..."

    print("You're all set!")