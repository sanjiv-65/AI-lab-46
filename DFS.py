#BFS to find shortest path and nodes explored
from collections import deque

def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = deque([(start, [start])]) 
    visited = set()
    visited.add(start)
    nodes_explored = 0

    while queue:
        (x, y), path = queue.popleft()
        nodes_explored += 1

        if (x, y) == end:
            return path, nodes_explored
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 1 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))

    return None, nodes_explored  
maze = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]
start = (0, 0) 
end = (4, 4)
bfs_path, bfs_nodes = bfs(maze, start, end)
print("BFS:")
print(f"Shortest Path: {bfs_path}")
print(f"Nodes Explored: {bfs_nodes}")


#DFS to find the depth continued unti when we dont find the goal
def main():
    lst = [
        [0 for _ in range(6)],
        [0, 1, 1, 1, 1, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 1, 1, 1, 3, 0],
        [0 for _ in range(6)]
    ]

    dfs(lst)

def dfs(maze):
    stack = []  # Use a stack instead of a queue
    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]

    count = 0
    start = [1, 4]
    visited[start[0]][start[1]] = True
    stack.append(start)

    while stack:
        pos = stack.pop()  # Pop the last added element (LIFO)
        print(f"Visiting: {pos}")

        if maze[pos[0]][pos[1]] == 3:
            print("Destination Found")
            break

        travel_x(maze, pos, stack, 1, visited)  # Move right
        travel_x(maze, pos, stack, -1, visited)  # Move left
        travel_y(maze, pos, stack, -1, visited)  # Move up
        travel_y(maze, pos, stack, 1, visited)  # Move down

        count += 1

    print("Cost:", count)

def travel_x(maze, pos, stack, i, visited):
    if 0 <= pos[1] + i < len(maze[0]):  # Check column bounds
        if maze[pos[0]][pos[1] + i] != 0 and not visited[pos[0]][pos[1] + i]:
            stack.append([pos[0], pos[1] + i])
            visited[pos[0]][pos[1] + i] = True

def travel_y(maze, pos, stack, i, visited):
    if 0 <= pos[0] + i < len(maze):  # Check row bounds
        if maze[pos[0] + i][pos[1]] != 0 and not visited[pos[0] + i][pos[1]]:
            stack.append([pos[0] + i, pos[1]])
            visited[pos[0] + i][pos[1]] = True


if __name__ == "__main__":
    main()