# Implements the depth first search algorithm


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


# O(v + e) time | O(v) space
def depth_first_search(root):
    nodes = [root]
    res = []

    while nodes:
        node = nodes.pop()
        res.append(node.value)

        for child in node.children[::-1]:
            nodes.append(child)
    
    return res


if __name__ == "__main__":
    root = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")
    f = Node("F")
    g = Node("G")
    h = Node("H")
    i = Node("I")
    j = Node("J")
    k = Node("K")
    root.children = [b, c, d]
    b.children = [e, f]
    d.children = [g, h]
    f.children = [i, j]
    g.children = [k]
    
    res = depth_first_search(root)

    assert res == ["A","B","E","F","I","J","C","D","G","K","H"], res

    print("You're all set!")