import heapq

class PriorityQueue:
    """Priority Queue using heapq (min-heap)."""

    def __init__(self):
        self.heap = []

    def enqueue(self, item, priority):
        """Insert an item with given priority (lower = higher priority)."""
        heapq.heappush(self.heap, (priority, item))

    def dequeue(self):
        """Remove and return the item with highest priority."""
        if self.is_empty():
            return "Queue is empty! Cannot dequeue."
        priority, item = heapq.heappop(self.heap)
        return item

    def display(self):
        """Print contents of the priority queue."""
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Priority Queue contents:")
            for priority, item in self.heap:
                print(f"Item: {item}, Priority: {priority}")

    def is_empty(self):
        """Check if queue is empty."""
        return len(self.heap) == 0


# Example usage
if __name__ == "__main__":
    pq = PriorityQueue()

    pq.enqueue("Task A", 3)
    pq.enqueue("Task B", 1)
    pq.enqueue("Task C", 2)

    pq.display()

    print("\nDequeued:", pq.dequeue())
    pq.display()
