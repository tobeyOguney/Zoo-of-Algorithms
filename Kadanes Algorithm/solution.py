# Implementation of Kadane's algorithm

# Well, I remember dynamic programming will be useful here
# Let's draw our table or array

# O(n) time | O(n) space
def kadanes_algo(lis):
    M = [0]
    idx_mem = []

    for i in range(len(lis)):
        max_val = max(lis[i], lis[i]+M[i])
        M.append(max_val)

        if max_val == lis[i]:
            idx_mem.append(i)
        else:
            idx_mem.append(idx_mem[-1])

    max_sum = max(M)

    val_idx = M.index(max_sum)
    start_idx = idx_mem[val_idx]

    return max_sum, lis[start_idx: val_idx]



if __name__ == "__main__":
    res = kadanes_algo(
        [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
    )

    assert res == (19, [1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1]), res

    print("You're all set!")
