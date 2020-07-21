# Solves the remove kth node from end problem


class LinkedList:
    def __init__(self, num):
        self.value = num
        self.next = None


def get_length(head):
    counter = 0

    node = head
    while node:
        node = node.next
        counter += 1
    
    return counter


# O(n) time | O(1) space
def remove_kth_node(head, k):
    length = get_length(head)

    counter = 0
    previous_node = None
    next_node = None

    node = head
    while node:
        if length - counter == k+1:
            previous_node = node
        
        if length - counter == k-1:
            next_node = node
        
        node = node.next
        counter += 1

    if previous_node:
        previous_node.next = next_node
        return head
    
    return head.next


if __name__ == "__main__":
    head = LinkedList(0)

    node = head
    for i in range(1, 10):
        node.next = LinkedList(i)
        node = node.next

    head = remove_kth_node(head, 10)

    node = head
    while node:
        print(node.value)
        node = node.next