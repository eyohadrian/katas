# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.

# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2

class MinStack:
    MAX_N = 999999999999999 
    def __init__(self):
        self.stack = []
        self.min = self.MAX_N

    def push(self, val: int) -> None:
        if self.min > val:
            self.min = val
        return self.stack.append(val)

    def pop(self) -> None:
        value=self.stack.pop()
        if value <= self.min:
            self.min = self.MAX_N
            for x in self.stack:
                if x < self.min:
                    self.min = x
        return value

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
