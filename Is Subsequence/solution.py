# Solution to the Is Subsequence problem

# Originally brought dynamic programming to mind.
# However, I'm currently thinking about validation in a single pass
# The latter approach does not seem like it can be clean to me - seems brutish.
# I'm going to try dynamic programming on it

# Dynamic programming doesn't work here, there's not useful pattern in the table
# I'm thinking of using the stack data structure here

# So I'm going to use two pointers here
# One pointing to the first character in s and the other to the first character in t
# Then we'd have a while loop that terminates whenever any pointer falls off
# > If the current character in t is equal to the current character in s, add it to the stack,
#   and increment to pointer to s by one.
# Confirm that the stack contains all the characters of s.


class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]


# O(m+n) time | O(n) space
def is_subsequence(s, t):
    first = 0           # Pointer assigned to s
    second = 0          # Pointer assigned to t

    stack = Stack()

    while first < len(s) and second < len(t):
        if t[second] == s[first]:
            stack.push(t[second])
            first += 1

        second += 1
    
    for idx in reversed( range( len(s) ) ):
        if s[idx] != stack.pop():
            return False
    
    return True

if __name__ == "__main__":
    first_result = is_subsequence("abc", "ahbgdc")
    second_result = is_subsequence("axc", "ahbgdc")

    assert first_result == True, "First test case failed."
    assert second_result == False, "Second test case failed."

    print("Both test cases passed.")