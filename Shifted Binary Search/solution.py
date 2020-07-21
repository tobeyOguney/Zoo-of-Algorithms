# Solves the shifted binary search problem

# O(lg n) time | O(1) space
def binary_search(lis, val):
    left_idx = 0
    right_idx = len(lis) - 1

    while left_idx <= right_idx:
        middle_idx = (left_idx + right_idx) // 2

        if lis[middle_idx] == val:
            return middle_idx
        
        elif lis[middle_idx] < val:
            left_idx = middle_idx + 1
        
        else:
            right_idx = middle_idx - 1
    
    return -1

# O(lg n) time | O(1) space
def shifted_binary_search(lis, val):
    left_idx = 0
    right_idx = len(lis) - 1

    while left_idx <= right_idx:
        middle_idx = (left_idx + right_idx) // 2

        if lis[middle_idx] == val:
            return middle_idx
        
        elif lis[left_idx] <= lis[middle_idx]:
            if lis[left_idx] <= val < lis[middle_idx]:
                right_idx = middle_idx - 1  
            
            else:
                left_idx = middle_idx + 1
        
        else:
            if lis[middle_idx] < val <= lis[right_idx]:
                left_idx = middle_idx + 1
            
            else:
                right_idx = middle_idx - 1
    
    return -1


if __name__ == "__main__":
    res = shifted_binary_search(
        [45, 61, 71, 72, 73, 0, 1, 21, 33, 45], 33
    )
    
    assert res == 8, res

    print("You're all set!")