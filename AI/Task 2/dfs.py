def dfs(graph, start):
    visited = {node: False for node in graph}
    parent = {start: None}
    stack = [start]

    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    parent[neighbor] = current
                    stack.append(neighbor)

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
dfs(graph, 0)
    
