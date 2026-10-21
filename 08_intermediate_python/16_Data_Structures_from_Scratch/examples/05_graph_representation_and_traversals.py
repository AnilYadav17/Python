"""
05_graph_representation_and_traversals.py
Pure Python Graph implementation using Adjacency List:
- Directed and Undirected edge insertion
- Breadth-First Search (BFS) for shortest path
- Depth-First Search (DFS) for reachable nodes traversal
"""

class PureGraph:
    def __init__(self, directed=False):
        self.adj_list = {}
        self.directed = directed

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj_list[u].append(v)
        if not self.directed:
            self.adj_list[v].append(u)

    def bfs_shortest_path(self, start, target):
        """
        BFS using pure list as queue to find shortest path in unweighted graph.
        Returns path as list of vertices.
        """
        if start not in self.adj_list or target not in self.adj_list:
            return None

        visited = {start}
        # Queue stores tuples of (current_vertex, path_so_far)
        queue = [(start, [start])]

        while queue:
            current, path = queue.pop(0)
            if current == target:
                return path

            for neighbor in self.adj_list.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        return None

    def dfs_traversal(self, start):
        """Iterative DFS using a pure stack."""
        if start not in self.adj_list:
            return []

        visited = set()
        traversal = []
        stack = [start]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                traversal.append(vertex)
                # Push unvisited neighbors in reverse order
                for neighbor in reversed(self.adj_list[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return traversal


def main():
    print("--- Pure Graph: Adjacency List & Traversals ---")
    g = PureGraph(directed=False)

    # Building graph of city connections:
    # A -- B -- D
    # |    |    |
    # C ---+----+
    g.add_edge("NYC", "BOS")
    g.add_edge("NYC", "PHL")
    g.add_edge("PHL", "DC")
    g.add_edge("BOS", "POR")
    g.add_edge("DC", "ATL")
    g.add_edge("BOS", "DC")

    print(f"Adjacency List:")
    for city, neighbors in g.adj_list.items():
        print(f"  {city:<5} -> {neighbors}")

    print("\n--- BFS Shortest Path ---")
    shortest_path = g.bfs_shortest_path("NYC", "ATL")
    print(f"Shortest path from NYC to ATL: {' -> '.join(shortest_path)}")

    print("\n--- DFS Reachable Traversal ---")
    visited_order = g.dfs_traversal("NYC")
    print(f"DFS Traversal Order starting from NYC: {' -> '.join(visited_order)}")

if __name__ == "__main__":
    main()
