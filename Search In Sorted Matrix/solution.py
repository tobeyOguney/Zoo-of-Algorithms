# Solves the search in sorted matrix problem


def search_in_sorted(matrix, val):
    row = 0
    col = len(matrix) - 1

    while row < len(matrix) and col >= 0:
        if matrix[row][col] > val:
            col -= 1
        elif matrix[row][col] < val:
            row += 1
        else:
            return [row, col]
    
    return [-1, -1]


if __name__ == "__main__":
    res = search_in_sorted(
        [ [1, 4, 7, 12, 15, 1000],
        [2, 5, 19, 31, 32, 1001],
        [3, 8, 24, 33, 35, 1002],
        [40, 41, 42, 44, 45, 1003],
        [99, 100, 103, 106, 128, 1004] ], 44
    )

    assert res == [3, 3], res

    print("You're all set!")