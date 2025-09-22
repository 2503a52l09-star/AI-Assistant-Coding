class Queue:
    """
    A simple FIFO (First-In, First-Out) queue implementation.
    """

    def __init__(self):
        self.items = []  # internal list to hold queue elements

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the front item of the queue."""
        if self.is_empty():
            return "Queue is empty! Cannot dequeue."
        return self.items.pop(0)

    def peek(self):
        """Return the front item without removing it."""
        if self.is_empty():
            return "Queue is empty! Nothing to peek."
        return self.items[0]

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)

    def is_empty(self):
        """Check whether the queue is empty."""
        return len(self.items) == 0


# Example usage
if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("Peek:", q.peek())      # 10
    print("Dequeue:", q.dequeue()) # 10
    print("Size:", q.size())       # 2
    print("Dequeue:", q.dequeue()) # 20
    print("Dequeue:", q.dequeue()) # 30
    print("Is Empty?", q.is_empty()) # True
    print("Dequeue:", q.dequeue()) # Queue is empty! Cannot dequeue.
