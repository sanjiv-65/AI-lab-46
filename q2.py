def dfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    stack = [(start, [start])]  # (current cell, path to current cell)
    visited = set()
    visited.add(start)
    nodes_explored = 0

    while stack:
        (x, y), path = stack.pop()
        nodes_explored += 1

        if (x, y) == end:
            return path, nodes_explored

        # Explore neighbors
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 1 and (nx, ny) not in visited:
                visited.add((nx, ny))
                stack.append(((nx, ny), path + [(nx, ny)]))

    return None, nodes_explored  # No path found
maze = [
      [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]
start = (0, 0)  # Top-left corner
end = (4, 4)    # Bottom-right corner
dfs_path, dfs_nodes = dfs(maze, start, end)
print("\nDFS:")
print(f"A Valid Path: {dfs_path}")
print(f"Nodes Explored: {dfs_nodes}")
