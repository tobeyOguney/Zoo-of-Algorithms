# Solves the single cycle check problem


def single_cycle_check(lis):
    was_visited = [False for _ in range(len(lis))]
    i = 0

    while not was_visited[i]:
        was_visited[i] = True
        i = (i + lis[i]) % len(lis)

    print(was_visited)
    
    return False if False in was_visited else True



if __name__ == "__main__":
    assert single_cycle_check([2, 3, 1, -4, -4, 2]) == True

    print("You're all set!")