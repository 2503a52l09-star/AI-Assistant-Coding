
def print_selection_table():
    """Prints the feature-to-data-structure mapping with justification."""
    table = [
        ["Student Attendance Tracking", "Deque",
         "Students enter and exit in real-time. Deque allows fast insert/remove from both ends."],
        ["Event Registration System", "Hash Table",
         "Quick search, insert, and delete needed. Hash table provides O(1) average operations."],
        ["Library Book Borrowing", "Binary Search Tree (BST)",
         "Books can be organized by due date/ID. BST allows efficient sorted insert, delete, and traversal."],
        ["Bus Scheduling System", "Graph",
         "Routes and stops are naturally modeled as a graph (nodes=stops, edges=routes)."],
        ["Cafeteria Order Queue", "Queue",
         "Orders must be served in First-In-First-Out (FIFO) order, so a queue is best."]
    ]

    print("\n=== Feature → Data Structure → Justification ===")
    print(f"{'Feature':<30} {'Data Structure':<20} Justification")
    print("-" * 80)
    for row in table:
        print(f"{row[0]:<30} {row[1]:<20} {row[2]}")


# -----------------------------------------------------------
# Part 2: AI-Generated Initial Code (Cafeteria Queue)
# -----------------------------------------------------------

class CafeteriaQueue:
    """
    A simple implementation of a cafeteria order queue.
    Uses FIFO (First-In, First-Out) principle.
    """

    def __init__(self):
        """Initialize an empty order queue."""
        self.queue = []

    def enqueue(self, order):
        """
        Add a new order to the queue.
        Args:
            order (str): Student's food order.
        """
        self.queue.append(order)

    def dequeue(self):
        """
        Serve (remove and return) the first order in the queue.
        Returns:
            str: The order that was served.
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot serve from an empty queue.")
        return self.queue.pop(0)

    def peek(self):
        """
        View the first order without removing it.
        Returns:
            str or None: The first order if available, else None.
        """
        return None if self.is_empty() else self.queue[0]

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0


# -----------------------------------------------------------
# Part 3: AI-Generated Test Cases
# -----------------------------------------------------------

def test_cafeteria_queue():
    """Run assert-based test cases for CafeteriaQueue."""
    q = CafeteriaQueue()

    # Test 1: Enqueue and Peek
    q.enqueue("Burger")
    assert q.peek() == "Burger", "Test 1 Failed: Peek should return 'Burger'"

    # Test 2: Enqueue more and Dequeue
    q.enqueue("Pizza")
    q.enqueue("Sandwich")
    assert q.dequeue() == "Burger", "Test 2 Failed: First served should be 'Burger'"

    # Test 3: Serve remaining orders
    assert q.dequeue() == "Pizza", "Test 3 Failed: Next served should be 'Pizza'"
    assert q.dequeue() == "Sandwich", "Test 3 Failed: Next served should be 'Sandwich'"

    # Test 4: Queue should now be empty
    assert q.is_empty() is True, "Test 4 Failed: Queue should be empty"

    print("✅ All CafeteriaQueue test cases passed!")


# -----------------------------------------------------------
# Part 4: Execution & Analysis
# -----------------------------------------------------------

if __name__ == "__main__":
    # Print mapping table
    print_selection_table()

    # Run test cases
    print("\n=== Running Test Cases ===")
    test_cafeteria_queue()

    # Final Analysis
    print("\n=== Analysis ===")
    print("✔ The Cafeteria Queue implementation correctly follows FIFO order.")
    print("✔ All assert-based test cases passed.")
    print("✔ Improved version includes docstrings and inline comments for clarity.")
