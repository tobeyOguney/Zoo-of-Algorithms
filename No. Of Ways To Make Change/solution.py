# Solves the no. of ways to make change problem


# O(td) time | O(t+d) space
def num_ways(target, denoms):
    # Adjust denoms for memo table offset
    denoms = [0] + denoms

    # Implement minified memo table
    memo = [
        [0 for _ in range(target+1)] for _ in range(2)
    ]

    memo[0][0] = 1
    memo[1][0] = 1

    for i in range(1, len(denoms)):        # Iterate over rows
        for j in range(1, target+1):    # Iterate over columns
            if denoms[i] == 1:          # The edge case of a unitary denomination
                memo[1][j] = 1
            
            elif not j % denoms[i]:
                memo[1][j] = memo[1][j-denoms[i]] + 1
            
            elif j > denoms[i]:
                if memo[1][j-denoms[i]]:
                    memo[1][j] = memo[1][j-denoms[i]] + 1
                else:
                    memo[1][j] = memo[0][j]
            
            elif j < denoms[i]:
                memo[1][j] = memo[0][j]
        
        # print(memo[1])      # Verify memo table

        memo[0] = list(memo[1])
    
    return memo[-1][-1]

if __name__ == "__main__":
    res = num_ways(
        6, [1, 5]
    )

    assert res == 2, res

    print("You're all set!")