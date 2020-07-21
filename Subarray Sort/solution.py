# Solves the subarray sort problem


def get_range(lis, min_val, max_val):
    first_idx = None
    last_idx = None

    for i in range(len(lis)):
        if min_val < lis[i]:
            first_idx = i
            break
    
    for i in range(len(lis))[::-1]:
        if max_val > lis[i]:
            last_idx = i
            break
    
    return [first_idx, last_idx]

def subarray_sort(lis):
    min_unsorted_val = float('inf')
    max_unsorted_val = float('-inf')

    for i in range(len(lis)-1):
        if lis[i] > lis[i+1]:
            min_unsorted_val = min(min_unsorted_val, lis[i+1])
            max_unsorted_val = max(max_unsorted_val, lis[i])
    
    if min_unsorted_val == float('inf'):
        return [-1, -1]
    
    return get_range(lis, min_unsorted_val, max_unsorted_val)

if __name__ == "__main__":
    res = subarray_sort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19])

    assert res == [3, 9], res

    print("You're all set!")