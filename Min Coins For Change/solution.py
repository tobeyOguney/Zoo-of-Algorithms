# Solution to the min. coins for change problem


# O(td) time | O(t+d) space
def min_coins(target, denoms):
    # Adjust denoms for memo table offset
    denoms = [0] + denoms

    # Implement minified memo table
    memo = [
        [0 for _ in range(target+1)] for _ in range(2)
    ]

    memo[0][0] = 0
    memo[1][0] = 0

    for i in range(1, len(denoms)):            # Loop over rows
        for j in range(1, target+1):           # Loop over columns
            if not j % denoms[i]:                      # Diagonal check
                memo[1][j] = memo[1][j-denoms[i]] + 1
            
            elif j > denoms[i]:
                memo[1][j] = memo[1][j-denoms[i]] + 1 if memo[1][j-denoms[i]] else memo[0][j]
            
            else:
                memo[1][j] = memo[0][j]

        # print(memo[1])

        memo[0] = list(memo[1])
    
    return memo[-1][-1] if memo[-1][-1] else -1


if __name__ == "__main__":
    res = min_coins(
        7, [1, 5, 10]
    )

    assert res == 3, res

    print("You're all set!")