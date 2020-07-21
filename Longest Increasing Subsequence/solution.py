# Solves the longest increasing subsequence problem


def get_result_lis(lis, memo):
    entry_point = max(enumerate(memo), key=lambda item: item[1][0])[0]
    res = []

    i = entry_point
    while i != None:
        res.append(lis[i])
        i = memo[i][1]

    return res[::-1]

# O(n^2) time | O(n) space
def longest_inc_subsq(lis):
    memo = []

    for i in range(len(lis)):
        pair = (0, None)
        for j in range(i):
            if lis[j] < lis[i]:
                pair = (memo[j][0]+1, j) if memo[j][0]+1 > pair[0] else pair
        memo.append(pair)
    # print(memo)
    return get_result_lis(lis, memo)

# O(lg n) time | O(1) space
def log_find_retiree_idx(idx, lis, indices, start, end):
    mid = (start + end)//2

    if start == end:
        return len(indices)

    if mid == start:
        return mid if lis[idx] <= lis[indices[mid]] else mid+1

    if lis[idx] < lis[indices[mid]]:
        return log_find_retiree_idx(idx, lis, indices, start, mid)
    
    if lis[idx] > lis[indices[mid]]:
        return log_find_retiree_idx(idx, lis, indices, mid+1, end)
    
    if lis[indices[mid]] == lis[idx]:
        return mid
    
# O(lg n) time | O(n) space
def update_indices(idx, lis, indices, memo):
    if not indices:
        indices.append(idx)
        memo.append(None)
    
    else:
        new_idx = log_find_retiree_idx(idx, lis, indices, 0, len(indices))
        
        if new_idx >= len(indices):
            indices.append(idx)
            memo.append(indices[-2])

        else:
            indices[new_idx] = idx

            if new_idx:
                memo.append(indices[new_idx-1])
            else:
                memo.append(None)

# O(nlg n) time | O(n) space
def logesqe_inc_subsq(lis):
    indices = []
    memo = []

    for i in range(len(lis)):
        update_indices(i, lis, indices, memo)
    
    # print(memo)
    
    return [lis[i] for i in indices]


if __name__ == "__main__":
    res = logesqe_inc_subsq(
        [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]
    )

    assert res == [-24, 2, 3, 5, 6, 35], res

    print("You're all set!")
