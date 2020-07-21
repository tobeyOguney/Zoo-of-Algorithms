# Implements the quick sort algorithm

# O(nlg n) time | O(lg n) space
def quick_sort(array):
    quick_sort_helper(array, 0, len(array)-1)

    return array

def quick_sort_helper(array, start_idx, end_idx):
    if start_idx >= end_idx:
        return
    
    pivot_idx = start_idx
    left_idx = pivot_idx + 1
    right_idx = end_idx

    while left_idx <= right_idx:
        if array[left_idx] > array[pivot_idx] and array[right_idx] < array[pivot_idx]:
            array[left_idx], array[right_idx] = array[right_idx], array[left_idx]
        
        if array[left_idx] <= array[pivot_idx]:
            left_idx += 1
        
        if array[right_idx] >= array[pivot_idx]:
            right_idx -= 1
    
    array[pivot_idx], array[right_idx] = array[right_idx], array[pivot_idx]

    if end_idx - right_idx - 1 > right_idx - 1 - start_idx:
        quick_sort_helper(array, start_idx, right_idx - 1)
        quick_sort_helper(array, right_idx + 1, end_idx)
    
    else:
        quick_sort_helper(array, right_idx + 1, end_idx)
        quick_sort_helper(array, start_idx, right_idx - 1)


if __name__ == "__main__":
    res = quick_sort([8, 5, 2, 9, 5, 6, 3])

    assert res == [2, 3, 5, 5, 6, 8, 9], res

    print("You're all set!")