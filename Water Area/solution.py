# Solves the water area problem


# O(n) time | O(n) space
def water_area(lis):
    # Implement memo
    memo = [0 for i in range(len(lis))]
    max_val = 0

    for i in range(len(lis)):
        max_val = max(max_val, lis[i])
        memo[i] = max_val
    
    max_val = 0
    for i in range(len(lis))[::-1]:
        max_val = max(max_val, lis[i])
        memo[i] = min(memo[i], max_val)
    
    print(memo)     # Verify memo

    return sum(
        [max(0, memo[i] - lis[i]) for i in range(len(lis))]
    )

if __name__ == "__main__":
    res = water_area([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3])

    assert res == 48, res

    print("You're all set!")