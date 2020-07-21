"""A representation of the min max stack"""

class MinMaxStack:
    def __init__(self):
        self.min_stack = []
        self.max_stack = []
        self.stack = []

    # O(1) time | O(1) space
    def peek(self):
        return self.stack[-1]

    # O(1) time | O(1) space
    def pop(self):
        self.min_stack.pop()
        self.max_stack.pop()
        return self.stack.pop()

    # O(1) time | O(1) space
    def push(self, val):
        if self.min_stack:
            self.min_stack.append(
                min(self.min_stack[-1], val)
            )
            self.max_stack.append(
                max(self.max_stack[-1], val)
            )
        else:
            self.min_stack.append(val)
            self.max_stack.append(val)

        self.stack.append(val)

    # O(1) time | O(1) space
    def get_min(self):
        return self.min_stack[-1]

    # O(1) time | O(1) space
    def get_max(self):
        return self.max_stack[-1]


if __name__ == "__main__":
    stk = MinMaxStack()
    stk.push(3)
    stk.push(5)
    stk.push(1)
    print("Max ", stk.get_max())
    print("Min ", stk.get_min())
    print("Last ", stk.peek())
    print(stk.pop())