# Solution to the knapsack problem

# This problem should not be jumped at
# You should take care to understand it as there are
# multiple variables with dynamic relationships to keep track of.

# We want to maximize value within the confines of weight

# O(n) time | O(n) space
def get_seq(memo, knapsack):
    i = len(memo) - 1           # Row pointer
    j = len(knapsack) - 1       # Column pointer
    seq = []

    while i > 0 and j > 0:
        if not memo[i][j] == memo[i][j-1]:
            seq.append(j-1)
            i -= knapsack[j][1]
            
        j -= 1
    
    return seq[::-1]

# O(nc) time | O(nc) space
def solve_knapsack(knapsack, max_weight):
    # Adjust knapsack for memo table offset
    knapsack = [None] + knapsack

    # Implement the memo table
    memo = [
        [0 for _ in range(len(knapsack))] for _ in range(max_weight+1)
    ]

    for i in range(1, len(memo)):      # Loop over the rows
        for j in range(1, len(knapsack)):  # Loop over the columns
            if knapsack[j][1] <= i:
                memo[i][j] = max(
                    memo[i][j-1], memo[i - knapsack[j][1]][j-1] + knapsack[j][0]
                )

            else:
                memo[i][j] = memo[i][j-1]

    # print(memo)       # View memo table for verification

    return [memo[-1][-1], get_seq(memo, knapsack)]


if __name__ == "__main__":
    knapsack = [[1, 2], [4, 3], [5, 6], [6, 7]]

    res = solve_knapsack(
        knapsack, 10
    )

    assert res == [10, [1, 3]], res

    print("You're all set!")
