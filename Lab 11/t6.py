class Graph:
    """Graph implementation using an adjacency list."""

    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        """Add a vertex if it does not exist."""
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, v1, v2):
        """Add an undirected edge between v1 and v2."""
        if v1 not in self.adj_list:
            self.add_vertex(v1)
        if v2 not in self.adj_list:
            self.add_vertex(v2)

        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)

    def display(self):
        """Print all vertices and their neighbors."""
        for vertex in self.adj_list:
            print(vertex, "->", " , ".join(self.adj_list[vertex]))


# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "D")

    print("Graph connections:")
    g.display()
