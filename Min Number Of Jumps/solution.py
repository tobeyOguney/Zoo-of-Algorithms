# Solves the min number of jumps problem


# O(n^2) time | O(n) space
def min_jumps(lis):
    jumps = [0]

    for i in range(1, len(lis)):
        min_jumps = float('inf')

        for j in range(i):
            if j + lis[j] >= i:
                min_jumps = min(min_jumps, jumps[j]+1)
        
        jumps.append(min_jumps)

    return jumps[-1]

# O(n) time | O(1) space
def linear_min_jumps(lis):
    jumps = 1
    steps = lis[0]
    max_idx = float('-inf')

    for i in range(1, len(lis)):
        max_idx = max(max_idx, i + lis[i])
        steps -= 1

        if steps == 0:
            steps = max_idx - i
            jumps += 1
    
    return jumps



if __name__ == "__main__":
    res = linear_min_jumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3])

    assert res == 4, res

    print("You're all set!")