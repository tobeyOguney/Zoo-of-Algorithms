# Implements the insertion sort algorithm


# O(n^2) time | O(1) space
def insertion_sort(lis):
    for i in range(1, len(lis)):
        current_item = lis.pop()
        is_last = True

        for j in range(i):
            if current_item < lis[j]:
                lis.insert(j, current_item)
                is_last = False
                break
        
        if is_last:
            lis.insert(i, current_item)



if __name__ == "__main__":
    lis = [8, 5, 2, 9, 5, 6, 3]
    insertion_sort(lis)

    assert lis == [2, 3, 5, 5, 6, 8, 9], lis

    print("You're all set!")