# Implements the breadth first search algorithm


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


# O(v + e) time | O(v) space
def breadth_first_search(node):
    nodes = [node]
    res = []

    while nodes:
        node = nodes.pop()
        res.append(node.value)
        
        for child in node.children:
            nodes.insert(0, child)
    
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
    
    res = breadth_first_search(root)

    assert res == ["A","B","C","D","E","F","G","H","I","J","K"], res

    print("You're all set!")