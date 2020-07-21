# Solves the min rewards problem

# O(n) time | O(n) space
def min_rewards(lis):
    memo = [0]
    min_val = [0, float('inf')]

    for i in range(1, len(lis)):
        if lis[i] < lis[i-1]:
             memo.append(memo[i-1]-1)
        elif lis[i] > lis[i-1]:
            memo.append(memo[i-1]+1)
        else:
            memo.append(memo[i-1])
        
        if min_val[1] > lis[i]:
            min_val = [i, lis[i]]
    
    offset = 1 - memo[min_val[0]]

    memo = [offset + val for val in memo]

    # Edge cases
    memo[0] = 1 if memo[0] < memo[1] else memo[0]
    memo[-1] = 1 if memo[-1] < memo[-2] else memo[-1]

    # print(memo)

    return sum(memo)


if __name__ == "__main__":
    res = min_rewards([8, 4, 2, 1, 3, 6, 7, 9, 5])

    assert res == 25, res

    print("You're all set!")