# Implements an LRU cache


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, node):
        if not self.head and not self.tail:
            self.head = node
            self.tail = node
        
        elif self.head != node:
            self.head.next = node
            node.prev = self.head
            self.head = node
    
    def peek_head(self):
        return self.head.value
    
    def pop_tail(self):
        if self.tail:
            node = self.tail
            self.tail = node.prev
            
            if self.tail:
                self.tail.next = None

            return node.value
        
        return None
    
    def set_head(self, node):
        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        self.add(node)


class LRUCache:
    # O(1) time
    def __init__(self, size):
        self.max_size = size or 1
        self.cache = dict()
        self.keys = DoublyLinkedList()

    # O(1) time
    def insert_key_value_pair(self, key, value):       
        if key not in self.cache:
            if len(self.cache) == self.max_size:
                self.pop_least_recent_key()

            node = Node((key, value))
            self.keys.add(node)
            self.cache[key] = node

        else:
            self.cache[key].value = (key, value)
    
    # O(1) time
    def get_most_recent_key(self):
        return self.keys.peek_head()[0]
    
    # O(1) time
    def pop_least_recent_key(self):
        least_recent = self.keys.pop_tail()
        del self.cache[least_recent[0]]

    # O(1) time
    def get_value_from_key(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.keys.set_head(node)
            return node.value[1]
        
        return None


if __name__ == "__main__":
    cache = LRUCache(3)
    cache.insert_key_value_pair("b", 2)
    cache.insert_key_value_pair("a", 1)
    cache.insert_key_value_pair("c", 3)
    assert cache.get_most_recent_key() == "c"
    assert cache.get_value_from_key("a") == 1
    assert cache.get_most_recent_key() == "a"
    cache.insert_key_value_pair("d", 4)
    assert cache.get_value_from_key("b") == None
    cache.insert_key_value_pair("a", 5)
    cache.get_value_from_key("a") == 5
    print("You're all set!")