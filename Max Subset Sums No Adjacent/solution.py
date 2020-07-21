# Solves the maximum subset sum with no adjaent elements problem


def max_sub_sum(lis):
    # Take care of the edge cases
    if len(lis) < 3:
        return 0
    elif len(lis) == 3:
        return lis[0] + lis[2]

    memo = [lis[0], lis[1], lis[0]+lis[2]]

    for i in range(3, len(lis)):
        memo.append(
            max(memo[i-2], memo[i-3]) + lis[i]
        )
    
    # print(memo)   # View memo for verification

    return max(memo)


if __name__ == "__main__":
    res = max_sub_sum([75, 105, 120, 75, 90, 135])

    assert res == 330, res

    print("You're all set!")