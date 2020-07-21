# Solves the branch sum problem

# The recursive solution is quite obvious
# Trying to think of other potential approaches, possibly iterative instead.
# Iterative solutions only work for DFS-based approaches for binary tree objects
# I can't use DFS here to construct a solution,
# so it seems that I am confined to the recursive solution.

# If the input was given in the form of an adjacency list, I could have an iterative solution.
# However, this is not the case.


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
def branch_sums(node):
    result = []
    
    if node:
        left_res = [node.value + val for val in branch_sums(node.left)]
        right_res = [node.value + val for val in branch_sums(node.right)]

        result.extend(left_res)
        result.extend(right_res)
    
        if not node.left and not node.right:
            result.append(node.value)
    
    return result
            

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

    # bt.print_tree()

    result = branch_sums(bt)

    assert set(result) == set([11, 21, 18, 15]), "Not quite there yet."

    print("You're all set!")