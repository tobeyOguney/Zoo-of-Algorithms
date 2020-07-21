# Implements the bubble sort algorithm

# O(n^2) time | O(1) space
def bubble_sort(lis):
    for _ in range(len(lis)):
        i = 0
        while i < len(lis)-1:
            if lis[i] > lis[i+1]:
                lis[i], lis[i+1] = lis[i+1], lis[i]
            
            i += 1


if __name__ == "__main__":
    lis = [8, 5, 2, 9, 5, 6, 3]

    bubble_sort(lis)

    assert lis == [2, 3, 5, 5, 6, 8, 9], lis

    print("You're all set!")