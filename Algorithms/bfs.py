def bfs(graph, start_node):
    # if start node or graph is empty then no solution
    if not (start_node and graph):
        return -1

    # create a set for tracking visited nodes
    visited = set()
    # created a queue for going through the nodes
    queue = [start_node]
    # loop will be executed until queue is not empty
    while queue:
        # fetching the front element of the queue
        current_node = queue.pop(0)  # checking if the node already visited or not
        # if visited then we won't print that node
        # otherwise, we will print the node and mark it as visited
        if current_node not in visited:
            print(current_node, end=" ")
            visited.add(current_node)
        # fetching the adjacent nodes of current node
        for vertex in graph[current_node]:
            if vertex not in visited:
                queue.append(vertex)


if __name__ == '__main__':
    graph = {
        '5': ['3', '7'],
        '3': ['2', '4'],
        '7': ['8'],
        '2': [],
        '4': ['8'],
        '8': []

    }
    bfs(graph, '5')
