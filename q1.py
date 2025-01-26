from collections import deque

def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = deque([(start, [start])]) 
    visited = set()
    visited.add(start)
    nodes_explored = 0
    cost=0

    while queue:
        (x, y), path = queue.popleft()
        nodes_explored += 1
        if(start)==end:
         return start,0
        if (x, y) == end:
            return path, nodes_explored

        # Explore neighbors
        for dx, dy in[(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 1 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))

    return None, nodes_explored  

# Example Maze and Start/End Points
maze = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]
start = (1, 2)  # Top-left corner
end = (3, 1)    # Bottom-right corner
bfs_path, bfs_nodes = bfs(maze, start, end)
print("BFS:")
print(f"Shortest Path: {bfs_path}")
print(f"Nodes Explored: {bfs_nodes}")
