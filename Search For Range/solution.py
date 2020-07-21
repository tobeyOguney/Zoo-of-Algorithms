# Solves the search for range problem


def left_bin_search(lis, num):
    left_idx = 0
    right_idx = len(lis) - 1

    while left_idx <= right_idx:
        middle_idx = (left_idx + right_idx) // 2
        if lis[middle_idx] == num and lis[middle_idx-1] != num:
            return middle_idx
        
        if lis[middle_idx] == num:
            right_idx = middle_idx - 1
        
        elif lis[middle_idx] < num:
            left_idx = middle_idx + 1
        
        else:
            right_idx = middle_idx - 1
    
    return -1


def right_bin_search(lis, num):
    left_idx = 0
    right_idx = len(lis) - 1

    while left_idx <= right_idx:
        middle_idx = (left_idx + right_idx) // 2
        if lis[middle_idx] == num and lis[middle_idx+1] != num:
            return middle_idx
        
        if lis[middle_idx] == num:
            left_idx = middle_idx + 1
        
        elif lis[middle_idx] < num:
            left_idx = middle_idx + 1
        
        else:
            right_idx = middle_idx - 1
    
    return -1
    

# O(lg n) time | O(1) space
def search_for_range(lis, num):
    left_idx = left_bin_search(lis, num)
    right_idx = right_bin_search(lis, num)

    return [left_idx, right_idx]


if __name__ == "__main__":
    res = search_for_range([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45)

    assert res == [4, 9], res

    print("You're all set!")