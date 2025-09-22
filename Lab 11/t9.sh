def print_table():
    """Prints a comparison table of data structures and their complexities."""

    table = [
        ["Array (static)", "O(1)", "O(n)", "O(n)", "O(n)", "Fixed size, random access efficient"],
        ["Dynamic Array (list)", "O(1) (amortized)", "O(n)", "O(1) amortized (append), O(n) insert", "O(n)", "Resizes automatically"],
        ["Stack", "O(n)", "O(n)", "O(1) push", "O(1) pop", "LIFO: Last In, First Out"],
        ["Queue", "O(n)", "O(n)", "O(1) enqueue", "O(1) dequeue", "FIFO: First In, First Out"],
        ["Deque", "O(n)", "O(n)", "O(1) both ends", "O(1) both ends", "Efficient double-ended queue"],
        ["Singly Linked List", "O(n)", "O(n)", "O(1) head / O(n) tail", "O(1) head / O(n) tail", "Sequential access only"],
        ["Doubly Linked List", "O(n)", "O(n)", "O(1) with pointer", "O(1) with pointer", "Supports traversal both ways"],
        ["Hash Table (dict)", "O(1) avg", "O(1) avg", "O(1) avg", "O(1) avg", "O(n) worst case (collisions)"],
        ["Binary Search Tree (BST)", "O(log n) avg", "O(log n) avg", "O(log n) avg", "O(log n) avg", "O(n) worst case (unbalanced)"],
        ["Balanced BST (AVL/Red-Black)", "O(log n)", "O(log n)", "O(log n)", "O(log n)", "Always balanced"],
        ["Heap (Priority Queue)", "O(n)", "O(n)", "O(log n)", "O(log n)", "Efficient for min/max retrieval"],
        ["Graph (Adjacency List)", "O(V+E)", "O(V+E)", "O(1) edge insert", "O(1) edge delete", "Efficient for sparse graphs"],
        ["Graph (Adjacency Matrix)", "O(1)", "O(1)", "O(1)", "O(1)", "Uses O(V^2) space"],
    ]

    headers = ["Data Structure", "Access", "Search", "Insertion", "Deletion", "Notes"]

    # Print table header
    print(f"{headers[0]:<28} {headers[1]:<15} {headers[2]:<15} {headers[3]:<25} {headers[4]:<15} {headers[5]}")
    print("-" * 120)

    # Print table rows
    for row in table:
        print(f"{row[0]:<28} {row[1]:<15} {row[2]:<15} {row[3]:<25} {row[4]:<15} {row[5]}")

# Run program
if __name__ == "__main__":
    print_table()
