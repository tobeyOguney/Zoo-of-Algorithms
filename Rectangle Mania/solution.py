# Solves the rectangle mania problem


def rectangle_mania_helper(point, fast_lis):
    top = (point[0], point[1]+1)
    right = (point[0]+1, point[1])
    adj = (point[0]+1, point[1]+1)

    if top in fast_lis:
        top_val = rectangle_mania_helper(top, fast_lis)
    else:
        top_val = -1
    
    if right in fast_lis:
        right_val = rectangle_mania_helper(right, fast_lis)
    else:
        right_val = -1

    if adj in fast_lis:
        val = 1
    else:
        val = -1
    
    return val + top_val + right_val + 2

# O(p) time | O(1) space
def rectangle_mania(lis):
    fast_lis = set(lis)
    return rectangle_mania_helper((0, 0), fast_lis)


if __name__ == "__main__":
    res = rectangle_mania(
        [(0, 0), (0, 1), (1, 1), (1, 0), (2, 1), (2, 0)]
    )

    assert res == 3, res

    print("You're all set!")