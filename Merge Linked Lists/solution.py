# Solution to the merge linked lists problem


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n+m) time | O(n+m) space
def merge_linked_list(node_1, node_2):
    first_node = node_1 if node_1.value < node_2.value else node_2
    second_node = node_2 if node_1.value < node_2.value else node_1

    while first_node.next:
        if second_node and first_node.next.value > second_node.value:
            temp_1 = first_node.next
            temp_2 = second_node.next
            first_node.next = second_node
            second_node.next = temp_1
            second_node = temp_2
        
        first_node = first_node.next


if __name__ == "__main__":
    node_1 = LinkedList(2)

    temp = node_1
    for num in [6, 7, 8]:
        temp.next = LinkedList(num)
        temp = temp.next

    node_2 = LinkedList(1)

    temp = node_2
    for num in [3, 4, 5, 9, 10]:
        temp.next = LinkedList(num)
        temp = temp.next

    merge_linked_list(node_1, node_2)

    is_correct = True
    temp = node_2
    for num in range(1, 11):
        if num != temp.value:
            is_correct = False
            
        temp = temp.next
    
    assert is_correct, "Not quite there yet..."

    print("You're all set!")
    