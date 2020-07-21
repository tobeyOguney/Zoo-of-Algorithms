# Solves the Find Loop problem


class Node:
    """Linked List implementation"""

    def __init__(self, val):
        self.value = val
        self.next = None

# What's the strategy to use here.

# I can see a solution where I'd traverse the list once,
# storing each node in a set and halting when a node is already
# a member of the set.

# This solution will give O(n) time and O(n) space

# Is it possible to have O(n) time and O(1) space?
# I guess I'll have to use some pointer magic.

# Odd and even pointers will meet each other in O(n) time and O(1) space
# Can we find the entry point into the cycle from this point in O(n) time and O(1) space?
# Sounds like a math problem to me.

# Like some modulo sh**
# Nope can't even be solved as a system of congruences in the simplest case

# O(n) time | O(1) space
def find_loop(node):
    first = node.next
    second = node.next.next
    counter = 1

    while first != second:
        first = first.next
        second = second.next.next
        counter += 1
    
    first = node

    while first != second:
        first = first.next
        second = second.next
    
    return first.value


if __name__ == "__main__":
    node = Node(0)

    temp = node
    node4 = None
    for i in range(1, 10):
        temp.next = Node(i)

        if i == 4:
            node4 = temp.next

        temp = temp.next

    temp.next = node4

    assert find_loop(node) == 4, "Not quite there yet."

    print("You're all set!")
    
