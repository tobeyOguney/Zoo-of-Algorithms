# An implementation of the topological sort algorithm


def get_child_map(jobs, deps):
    child_map = {job: [] for job in jobs}

    for dep in deps:
        child_map[dep[0]].append(dep[1])
    
    return child_map

def get_preq_map(jobs, deps):
    preq_map = {job: 0 for job in jobs}
    
    for dep in deps:
        preq_map[dep[1]] += 1
    
    return preq_map

# O(j + d) time | O(j + d) space
def topological_sort(jobs, deps):
    child_map = get_child_map(jobs, deps)
    preq_map = get_preq_map(jobs, deps)
    no_preq_nodes = [node for node in preq_map if preq_map[node] == 0]

    res = []
    while no_preq_nodes:
        node = no_preq_nodes.pop()

        for child_node in child_map[node]:
            preq_map[child_node] -= 1
            if preq_map[child_node] == 0:
                no_preq_nodes.append(child_node)

        res.append(node)
    
    return res if len(res) == len(jobs) else []


if __name__ == "__main__":
    res = topological_sort(
        {1, 2, 3, 4}, [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]
    )

    assert res in [[1, 4, 3, 2], [4, 1, 3, 2]], res

    print("You're all set!")