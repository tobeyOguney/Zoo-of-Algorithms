# Solves the max sum increasing subsequence problem

# O(n) time | O(n) space
def get_subsq(memo, lis):
    idx = memo.index(max(memo))
    subsq = [lis[idx]]

    for i in range(idx)[::-1]:
        if lis[i] < lis[idx] and memo[i] == memo[idx] - lis[idx]:
            subsq.append(lis[i])
            idx = i
    
    return subsq[::-1]

# O(n^2) time | O(n) space
def max_sum_subsq(lis):
    memo = []

    for i in range(len(lis)):
        max_val = 0
        for j in range(i):
            if lis[j] < lis[i]:
                max_val = memo[j] if memo[j] > max_val else max_val
        
        memo.append(max_val + lis[i])
    
    # print(memo)     # Verify memo

    return [max(memo), get_subsq(memo, lis)]


if __name__ == "__main__":
    res = max_sum_subsq([10, 70, 20, 30, 50, 11, 30])

    assert res == [110, [10, 20, 30, 50]], res

    print("You're all set!")