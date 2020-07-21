# Solves the Node Depth Sum problem

# Based on the input not being an adjacency list,
# The solution will have to be recursive as it is a traversal problem.


class BinaryTree:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
    
    def print_tree(self):
        if self.left:
            print(f"{self.value}: Left {self.left.value}.")
            self.left.print_tree()

        if self.right:
            print(f"{self.value}: Right {self.right.value}.")
            self.right.print_tree()

# O(n) time | O(n) space
def node_depth_sum(node, depth=0):
    if not node:
        return 0

    left_sum = node_depth_sum(node.left, depth+1)
    right_sum = node_depth_sum(node.right, depth+1)

    return depth + left_sum + right_sum


if __name__ == "__main__":
    bt = BinaryTree(6)
    bt_list = []

    for element in [3, 5, 2, 5, 4, 7, 4]:
        bt_list.append(BinaryTree(element))
    
    bt.left = bt_list[0]
    bt.right = bt_list[1]

    bt_list[0].left = bt_list[2]
    bt_list[0].right = bt_list[3]

    bt_list[1].right = bt_list[4]

    bt_list[3].left = bt_list[5]
    bt_list[3].right = bt_list[6]

    result = node_depth_sum(bt)

    assert result == 14, "Not quite there yet."

    print("You're all set")