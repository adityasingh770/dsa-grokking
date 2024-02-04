from collections import deque


def bfs(graph, start, item):
    """
    Perform Breadth-First Search (BFS) on a directed graph to find a specific item.

    Parameters:
    - graph (dict): An adjacency list representation of the directed graph.
                    The keys are nodes, and the values are lists of neighboring nodes.
    - start (int): The starting node for BFS.
    - item: The item to search for within the graph.

    Returns:
    bool: True if the item is found, False otherwise.

    Notes:
    - This function extends the basic BFS by searching for a specific item within the graph.
    - It explores the graph in breadth-first order, visiting nodes level by level.
    - The search stops and returns True as soon as the specified item is found.
    - The 'visited' set ensures that each node is processed only once.
    """
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(f"Visiting node {node}")
            if node == item:
                return True
            visited.add(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
    return False
