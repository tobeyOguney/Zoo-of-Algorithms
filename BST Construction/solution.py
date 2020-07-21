"""Implements the binary search tree"""

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    # O(lg n) time | O(1) space
    def insert(self, value):
        node = self

        while True:
            if node.value > value:
                if node.left:
                    node = node.left

                else:
                    node.left = BST(value)
                    break

            else:
                if node.right:
                    node = node.right

                else:
                    node.right = BST(value)
                    break
    
        return self
    
    # O(lg n) time | O(1) space
    def contains(self, value):
        node = self

        while node:
            if node.value == value:
                return True

            elif node.value > value:
                node = node.left

            else:
                node = node.right
        
        return False
    
    def remove(self, value, parent=None):
        node = self if not parent else parent

        while node:
            if node.value > value:
                parent = node
                node = node.left

            elif node.value < value:
                parent = node
                node = node.right

            else:
                if node.left and node.right:
                    node.value = node.right.get_min_val()
                    node.right.remove(node.value, node)
                    break

                elif node.left:
                    node.value = node.left.value
                    node.left, node.right = node.left.left, node.left.right

                elif node.right:
                    node.value = node.right.value
                    node.left, node.right = node.right.left, node.right.right

                else:
                    if not parent:
                        node.value = None
                        break

                    if parent.left == node:
                        parent.left = None
                    
                    elif parent.right == node:
                        parent.right = None
                    
                    break

        return self

    def get_min_val(self):
        node = self

        while node.left:
            node = node.left

        return node.value
    
    def print_tree(self):
        if self.left and self.right:
            print(f"{self.value} : {self.left.value} Left, {self.right.value} Right.")
        elif self.left:
            print(f"{self.value} : {self.left.value} Left.")
        elif self.right:
            print(f"{self.value} : {self.right.value} Right.")

        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()

if __name__ == '__main__':
    bst = BST(8)
    bst.insert(5)
    bst.insert(11)
    bst.insert(-1)
    bst.insert(3)
    bst.insert(4)
    bst.insert(2)
    bst.print_tree()
