from collections import deque

class DequeDS:
    """Double-ended queue using collections.deque."""

    def __init__(self):
        self.deque = deque()

    def insert_front(self, item):
        """Insert an item at the front."""
        self.deque.appendleft(item)

    def insert_rear(self, item):
        """Insert an item at the rear."""
        self.deque.append(item)

    def remove_front(self):
        """Remove and return the front item."""
        if self.is_empty():
            return "Deque is empty! Cannot remove front."
        return self.deque.popleft()

    def remove_rear(self):
        """Remove and return the rear item."""
        if self.is_empty():
            return "Deque is empty! Cannot remove rear."
        return self.deque.pop()

    def is_empty(self):
        """Check if the deque is empty."""
        return len(self.deque) == 0

    def display(self):
        """Print current contents of deque."""
        if self.is_empty():
            print("Deque is empty.")
        else:
            print("Deque contents:", list(self.deque))


# Example usage
if __name__ == "__main__":
    dq = DequeDS()

    dq.insert_rear(10)
    dq.insert_rear(20)
    dq.insert_front(5)
    dq.insert_front(1)

    dq.display()  # [1, 5, 10, 20]

    print("Removed Front:", dq.remove_front())  # 1
    print("Removed Rear:", dq.remove_rear())    # 20

    dq.display()  # [5, 10]
