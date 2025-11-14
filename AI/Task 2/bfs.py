from queue import Queue

def bfs(graph, start):
    q = Queue()
    q.put(start)

    visited = {node: False for node in graph}
    parent = {start: None}
    visited[start] = True

    while not q.empty():
        node = q.get()
        print(node, end=' ')

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = node
                q.put(neighbor)

    print("\n")

    for node in graph:
        path = []
        current = node
        while current is not None:
            path.append(current)
            current = parent[current]
        path.reverse()
        print(f"path to node {node}: {path}")


graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}

bfs(graph, 0)

