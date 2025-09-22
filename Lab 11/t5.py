class HashTable:
    """Simple Hash Table implementation using chaining."""

    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # list of buckets

    def _hash(self, key):
        """Generate an index for a given key."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert or update a key-value pair."""
        index = self._hash(key)
        bucket = self.table[index]

        # Update if key exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # Otherwise, insert new key-value
        bucket.append((key, value))

    def search(self, key):
        """Search for a key and return its value (or None)."""
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        """Delete a key-value pair if it exists."""
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False

    def display(self):
        """Print the hash table contents."""
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")


# Example usage
if __name__ == "__main__":
    ht = HashTable(size=5)

    ht.insert("apple", 100)
    ht.insert("banana", 200)
    ht.insert("grape", 300)
    ht.insert("orange", 400)

    print("Search apple:", ht.search("apple"))
    print("Search banana:", ht.search("banana"))

    ht.delete("banana")
    print("Search banana after delete:", ht.search("banana"))

    print("\nFinal Hash Table:")
    ht.display
