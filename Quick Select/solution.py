# Solves the quick select problem

# O(n) time | O(1) space
def quick_select(lis, k):
    return quick_select_helper(lis, k, 0, len(lis)-1)

def quick_select_helper(lis, k, start_idx, end_idx):
    if end_idx - start_idx == 1:
        return lis[start_idx]
    
    pivot_idx = start_idx
    left_idx = start_idx + 1
    right_idx = end_idx

    while left_idx <= right_idx:
        if lis[left_idx] > lis[pivot_idx] and lis[right_idx] < lis[pivot_idx]:
            lis[left_idx], lis[right_idx] = lis[right_idx], lis[left_idx]
        
        if lis[left_idx] <= lis[pivot_idx]:
            left_idx += 1
        
        if lis[right_idx] >= lis[pivot_idx]:
            right_idx -= 1
    
    lis[pivot_idx], lis[right_idx] = lis[right_idx], lis[pivot_idx]

    if right_idx == k-1:
        return lis[right_idx]
    
    if right_idx < k-1:
        return quick_select_helper(lis, k, right_idx+1, end_idx)
    
    return quick_select_helper(lis, k, start_idx, right_idx-1)


if __name__ == "__main__":
    res = quick_select([8, 5, 2, 9, 7, 6, 3], 3)

    assert res == 5, res

    print("You're all set!")