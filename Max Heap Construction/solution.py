"""Represents the min heap"""

class MinHeap:

    def __init__(self, arr):
        self.heap = self.build_heap(arr)
    
    # O(nlg n) time | O(1) space
    def build_heap(self, arr):
        first_parent_idx = (len(arr) - 2) // 2

        for current_idx in reversed(range(first_parent_idx + 1)):
            self.heapify_down(current_idx, len(arr)-1, arr)
        
        return arr

    # O(lg n) time | O(1) space
    def heapify_down(self, current_idx, end_idx, heap):
        left_child_idx = current_idx*2 + 1

        while left_child_idx <= end_idx:
            right_child_idx = current_idx*2 + 2 if current_idx*2 + 2 <= end_idx else -1

            if right_child_idx != -1 and heap[right_child_idx] < heap[left_child_idx]:
                idx_to_swap = right_child_idx
                
            else:
                idx_to_swap = left_child_idx

            if heap[current_idx] > heap[idx_to_swap]:
                heap[current_idx], heap[idx_to_swap] = heap[idx_to_swap], heap[current_idx]
                current_idx = idx_to_swap
                left_child_idx = current_idx*2 + 1
            
            else:
                return

    # O(lg n) time | O(1) space
    def heapify_up(self, current_idx, heap):
        parent_idx = (current_idx - 1) // 2

        while current_idx > 0 and heap[current_idx] < heap[parent_idx]:
            heap[current_idx], heap[parent_idx] = heap[parent_idx], heap[current_idx]
            current_idx = parent_idx
            parent_idx = (current_idx - 1) // 2

    # O(1) time | O(1) space
    def peek(self):
        return self.heap[0]

    # O(lg n) time | O(1) space
    def remove(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        smallest = self.heap.pop()
        self.heapify_down(0, len(self.heap)-1, self.heap)
        return smallest

    # O(lg n) time | O(1) space
    def insert(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap)-1, self.heap)


if __name__ == "__main__":
    arr = [9, 102, 30, 12, 18, 23, 31, 17, 44]
    mh = MinHeap(arr)
    print(mh.remove())
    print(mh.heap)