# Solves the reverse linked list problem


class LinkedList:
    def __init__(self, num):
        self.value = num
        self.next = None


# O(n) time | O(1) space
def reverse_linked_list(head):
    previous = None
    current = head

    while current:
        next_ = current.next
        current.next = previous
        previous = current
        current = next_
    
    return previous


if __name__ == "__main__":
    head = LinkedList(0)

    node = head
    for i in range(1, 6):
        node.next = LinkedList(i)
        node = node.next if node else node
    
    head = reverse_linked_list(head)

    node = head
    while node:
        print(node.value)
        node = node.next
