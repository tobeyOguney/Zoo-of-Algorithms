# Solves the largest range problem


def largest_range(lis):
    was_visited = {num: False for num in lis}
    max_range = [0, 0]

    for num in lis:
        if was_visited[num]:
            continue

        left = num
        while left in was_visited:
            was_visited[left] = True
            left -= 1
        
        right = num
        while right in was_visited:
            was_visited[right] = True
            right += 1
        
        max_range = [left+1, right-1] if right-left-2 > max_range[1]-max_range[0] else max_range
    
    return max_range




if __name__ == "__main__":
    res = largest_range([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6])

    assert res == [0, 7], res

    print("You're all set!")