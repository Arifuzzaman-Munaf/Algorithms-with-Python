def dfs(graph, start_node):
    # if start node or graph is empty then no solution
    if not (start_node and graph):
        return -1

    # creat a set for tracking visited nodes
    visited = set()
    # created a stack for going through the nodes
    stack = [start_node]
    # loop will be executed until stack is not empty
    while stack:
        # fetching the top element of the stack
        current_node = stack.pop()
        # checking if the node already visited or not
        # if visited then we won't print that node
        # otherwise, we will print the node and mark it as visited
        if current_node not in visited:
            print(current_node, end=" ")
            visited.add(current_node)
        # fetching the adjacent nodes of current node
        for vertex in graph[current_node]:
            if vertex not in visited:
                stack.append(vertex)


if __name__ == '__main__':
    graph = {
        '2': ['1', '5'],
        '5': ['6', '8'],
        '6': ['9'],
        '9': [],
        '8': [],
        '1': []

    }
    dfs(graph, '2')
