from collections import defaultdict, deque

def input_graph_as_list():
    """Take user input to create a graph as an edge list."""
    n = int(input("Enter the number of nodes in the graph: "))
    e = int(input("Enter the number of edges in the graph: "))
    
    print("Enter the edges as pairs of nodes (e.g., 0 1 for an edge between node 0 and 1):")
    graph = defaultdict(list)
    for _ in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)  
    return graph, n

def bidirectional_search(graph, start, goal):
    """Perform Bidirectional Search to find the shortest path."""
    if start == goal:
        return [start]
    forward_queue = deque([start])
    backward_queue = deque([goal])
    forward_visited = {start: None}
    backward_visited = {goal: None}
    def is_intersecting():
        return set(forward_visited.keys()) & set(backward_visited.keys())

    while forward_queue and backward_queue:
        if forward_queue:
            current_forward = forward_queue.popleft()
            for neighbor in graph[current_forward]:
                if neighbor not in forward_visited:
                    forward_visited[neighbor] = current_forward
                    forward_queue.append(neighbor)
        if backward_queue:
            current_backward = backward_queue.popleft()
            for neighbor in graph[current_backward]:
                if neighbor not in backward_visited:
                    backward_visited[neighbor] = current_backward
                    backward_queue.append(neighbor)
        intersection = is_intersecting()
        if intersection:
            meeting_node = next(iter(intersection))
            return reconstruct_bidirectional_path(forward_visited, backward_visited, start, goal, meeting_node)
    return None 
def reconstruct_bidirectional_path(forward_visited, backward_visited, start, goal, meeting_node):
    """Reconstruct the path from start to goal through the meeting node."""
    path = []
    current = meeting_node
    while current is not None:
        path.append(current)
        current = forward_visited[current]
    
    path.reverse()
    current = backward_visited[meeting_node]
    while current is not None:
        path.append(current)
        current = backward_visited[current]
    return path
if __name__ == "__main__":
    graph, num_nodes = input_graph_as_list()
    print("\nGraph (Adjacency List Representation):")
    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")
    start = int(input("\nEnter the start node (0 to {}): ".format(num_nodes - 1)))
    goal = int(input("Enter the goal node (0 to {}): ".format(num_nodes - 1)))
    path = bidirectional_search(graph, start, goal)
    if path:
        print("\nShortest path from {} to {}:".format(start, goal), path)
    else:
        print("\nNo path found from {} to {}.".format(start, goal))