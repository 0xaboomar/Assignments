def dfs(graph, start, target):
    visited = {node: False for node in graph}
    parent = {start: None}
    stack = [start]

    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True

            if current == target:
                break

            for neighbor in graph[current]:
                if not visited[neighbor]:
                    parent[neighbor] = current
                    stack.append(neighbor)

    path = []
    current = target
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()

    print(f"path to the target node {target}: {path}")


graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}

dfs(graph, 0, 4)
