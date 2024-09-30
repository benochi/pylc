class MinStack:

    def __init__(self):
        # two stacks  so we can track lowest val
        self.stack = []
        self.minStack = []

    # handle adding to stack, and min stack will track our lowest value.
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            self.minStack.append(min(val, self.minStack[-1]))
        else:
            self.minStack.append(val)

    # pop from both stacks, so indexes match for minVal.
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    # return last value of stack.
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


obj = MinStack()
obj.push(3)
obj.push(5)
print(obj.getMin())  # Output: 3
obj.push(2)
print(obj.getMin())  # Output: 2
obj.pop()
print(obj.getMin())  # Output: 3
