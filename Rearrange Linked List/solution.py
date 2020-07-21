# Solves the rearrange linked list problem


class LinkedList:
    def __init__(self, num):
        self.value = num
        self.next = None


# O(n) time | O(1) space
def rearrange_linked_list(head, k):
    last_smaller = None
    last_equal = None
    last_larger = None

    node = head
    while node:
        if node.value < k:
            if last_smaller:
                last_smaller.next = node
            else:
                first_smaller = node
            last_smaller = node
        
        if node.value == k:
            if last_equal:
                last_equal.next = node
            else:
                first_equal = node
            last_equal = node
        
        if node.value > k:
            if last_larger:
                last_larger.next = node
            else:
                first_larger = node
            last_larger = node
        
        node = node.next
    
    if last_equal:
        last_equal.next = first_larger
    
    if last_smaller:
        last_smaller.next = first_equal
        return first_smaller
    
    return first_equal


if __name__ == "__main__":
    head = LinkedList(3)

    node = head
    for i in [0, 5, 2, 1, 4]:
        node.next = LinkedList(i)
        node = node.next if node else node
    
    head = rearrange_linked_list(head, 0)

    node = head
    while node:
        print(node.value)
        node = node.next
