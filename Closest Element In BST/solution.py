# Solution to the closest element in BST problem

# The obvious solution will be to parse through the tree using DFS,
# while maintaining a "closest_element" variable
# That will give me a solution in O(m) time and O(1) space


class BinarySearchTree:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
    
    def insert(self, val):
        node = self

        while True:
            if val <= node.value:   # I made duplicate values to be stored to the left of each node
                if not node.left:
                    node.left = BinarySearchTree(val)
                    break

                else:
                   node = node.left 

            elif val > node.value:
                if not node.right:
                    node.right = BinarySearchTree(val)
                    break
                
                else:
                    node = node.right
    
    def print_tree(self):
        if self.left:
            print(f"{self.value}: Left {self.left.value}.")
            self.left.print_tree()

        if self.right:
            print(f"{self.value}: Right {self.right.value}.")
            self.right.print_tree()


# O(lg n) time | O(1) space
def find_closest_element(node, target):
    closest_element = node.value
    
    while True:
        if target < node.value:
            if not node.left:
                break

            closest_element = node.left.value if abs(node.left.value - target) < abs(closest_element - target) else closest_element
            node = node.left
        
        elif target > node.value:
            if not node.right:
                break

            closest_element = node.right.value if abs(node.right.value - target) < abs(closest_element - target) else closest_element
            node = node.right
        
        else:
            closest_element = node.value
            break
    
    return closest_element



if __name__ == "__main__":
    bst = BinarySearchTree(9)

    for element in [4, 17, 3, 6, 22, 5, 7, 20]:
        bst.insert(element)

    # bst.print_tree()

    target = 18

    result = find_closest_element(bst, target)

    assert result ==  17, "Not quite there yet."

    print("You're all set!")