class Stack:
    """
    A simple implementation of a stack (LIFO: Last-In, First-Out).
    """

    def __init__(self):
        self.items = []  # internal list to hold stack elements

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item of the stack."""
        if self.is_empty():
            return "Stack is empty! Cannot pop."
        return self.items.pop()

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            return "Stack is empty! Nothing to peek."
        return self.items[-1]

    def is_empty(self):
        """Check whether the stack is empty."""
        return len(self.items) == 0


# Example usage
if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)

    print("Peek:", s.peek())       # 30
    print("Pop:", s.pop())         # 30
    print("Is Empty?", s.is_empty())  # False
    print("Pop:", s.pop())         # 20
    print("Pop:", s.pop())         # 10
    print("Is Empty?", s.is_empty())  # True
    print("Pop:", s.pop())         # Stack is empty! Cannot pop.
