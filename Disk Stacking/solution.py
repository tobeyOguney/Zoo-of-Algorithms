# Solves the disk stacking problem


# O(n^2) time | O(n) space
def stack_disks(lis):
    # Sort by width
    lis.sort(key=lambda item: item[0])

    memo = []
    heights = []

    for i in range(len(lis)):
        stack = []
        max_height = 0

        for j in range(i):
            if lis[i][1] >  lis[j][1] and lis[i][2] > lis[j][2]:
                if heights[j] > max_height:
                    stack = memo[j]
                    max_height = heights[j]
        
        memo.append(stack + [lis[i]])
        heights.append(max_height + lis[i][2])
    
    # print(memo)   # Verify memo

    return memo[heights.index(max(heights))]



if __name__ == "__main__":
    res = stack_disks([[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]])

    assert res == [[2, 1, 2], [3, 2, 3], [4, 4, 5]], res

    print("You're all set!")