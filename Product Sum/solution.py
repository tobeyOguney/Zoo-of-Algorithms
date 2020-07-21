# Solution to the Node Depth Sum problem

# The recursive solution to this problem is quite obvious, and may max out call stack memory,
# I'm going to try out an iterative solution.


# O(n) time | O(n) space
def product_sum(arr):
    htbl = dict()
    temp_arr = arr
    idx = 0
    depth = 1

    htbl[depth] = [None, idx, 1]   # Tuple of parent array, index at parent array, and multiplier

    result = 0

    while True:
        if idx < len(temp_arr):
            if type(temp_arr[idx]) == type(list()):
                depth += 1
                multiplier = htbl[depth-1][2] * depth

                htbl[depth] = [temp_arr, idx+1, multiplier]

                temp_arr = temp_arr[idx]
                idx = 0

            result += temp_arr[idx] * htbl[depth][2]
            idx += 1
        
        else:
            if htbl[depth][0]:
                temp_arr, idx, _ = htbl[depth]
                depth -= 1

            else:
                break
        
    return result

            

if __name__ == "__main__":
    array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]

    result = product_sum(array)

    assert result == 12, "Not quite there yet."

    print("You're all set!")