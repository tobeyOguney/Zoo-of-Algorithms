# Solves the shift linked list problem


class LinkedList:
    def __init__(self, val):
        self.value = val
        self.next = None

    
def get_length(head):
    counter = 0
    node = head
    
    while node:
        counter += 1
        node = node.next

    return counter

# O(n) time | O(1) space
def shift_linked_list(head, k):
    length = get_length(head)

    counter = 0
    node = head
    while node:
        if counter == length - k - 1:
            new_tail = node
            new_head = node.next
        
        if counter == length - 1:
            old_tail = node

        node = node.next
        counter += 1
    
    new_tail.next = None
    old_tail.next = head

    return new_head


if __name__ == "__main__":
    head = LinkedList(0)

    node = head
    for i in range(1, 6):
        node.next = LinkedList(i)
        node = node.next
    
    head = shift_linked_list(head, 2)

    node = head
    while node:
        print(node.value)
        node = node.next
    