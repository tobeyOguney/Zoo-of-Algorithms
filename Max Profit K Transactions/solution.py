# Solution to the max profit k transactions problem


def max_profit(lis, k):
    # Implement the minified memo table
    memo = [
        [0 for _ in range(len(lis))] for _ in range(2)
    ]

    for _ in range(1, k+1):              # Iterate over the rows of the actual memo table
        min_idx = 0
        for j in range(1, len(lis)):   # Iterate over the columns of the memo table
            diff = lis[j] - lis[min_idx]
            memo[1][j] = max(diff, memo[1][j-1]) + memo[0][min_idx]
            min_idx = j if lis[j] < lis[min_idx] else min_idx
        
        # print(memo[1])                  # View memo table for verification

        memo[0] = list(memo[1])         # Create space for the next row of memo table
    
    return memo[-1][-1]


if __name__ == "__main__":
    res = max_profit(
        [5, 11, 3, 50, 60, 90], 2
    )

    assert res == 93, res

    print("You're all set!")