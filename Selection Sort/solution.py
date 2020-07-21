# Implements the selection sort algorithm


# O(n^2) time | O(1) space
def selection_sort(lis):
    for i in range(len(lis)):
        min_idx = None
        min_val = lis[i]
        for j in range(i, len(lis)):
            if lis[j] < min_val:
                min_idx = j
                min_val = lis[j]
        
        if min_idx:
            lis[i], lis[min_idx] = lis[min_idx], lis[i]


if __name__ == "__main__":
    lis = [8, 5, 2, 9, 5, 6, 3]

    selection_sort(lis)

    assert lis == [2, 3, 5, 5, 6, 8, 9], lis

    print("You're all set!")