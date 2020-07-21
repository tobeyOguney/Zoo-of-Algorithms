# Solves the right smaller than problem


class RS_BST:
    def __init__(self, value):
        self.value = value
        self.left_sub_size = 0
        self.left = None
        self.right = None

    def insert(self, value, idx, right_smaller_counts, num_currently_smaller=0):
        node = self

        while True:
            if node.value > value:
                node.left_sub_size += 1

                if node.left:
                    node = node.left

                else:
                    node.left = RS_BST(value)
                    right_smaller_counts[idx] = num_currently_smaller
                    break

            else:
                num_currently_smaller += node.left_sub_size

                if value > node.value:
                    num_currently_smaller += 1

                if node.right:
                    node = node.right

                else:
                    node.right = RS_BST(value)
                    right_smaller_counts[idx] = num_currently_smaller
                    break
    
        return self
    

def right_smaller_than(lis):
    right_smaller_counts = [0 for i in range(len(lis))]
    bst = RS_BST(lis[-1])

    for i in reversed(range(len(lis)-1)):
        bst.insert(lis[i], i, right_smaller_counts)
    
    return right_smaller_counts


if __name__ == "__main__":
    res = right_smaller_than([8, 5, 11, -1, 3, 4, 2])
    
    assert res == [5, 4, 4, 0, 1, 1, 0], res

    print("You're all set!")