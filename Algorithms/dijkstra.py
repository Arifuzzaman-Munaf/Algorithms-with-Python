import heapq


def dijkstra(graph, start):
    visited = set()
    distance = {vertex: float("inf") for vertex in graph.keys()}
    distance[start] = 0

    min_heap = [(0, start)]

    while min_heap:

        current_distance, current_node = heapq.heappop(min_heap)
        if current_node in visited:
            continue

        visited.add(current_node)
        if len(visited) == len(graph.keys()):
            return distance

        for node, dist in graph[current_node]:
            new_distance = current_distance + dist
            if new_distance < distance[node] and node not in visited:
                distance[node] = new_distance
                heapq.heappush(min_heap, (new_distance, node))
    return -1


if __name__ == '__main__':
    graph = {
        'A': [('B', 1.8), ('C', 1.5), ('D', 1.4)],
        'B': [('A', 1.8), ('E', 1.6)],
        'C': [('A', 1.5), ('E', 1.8), ('F', 2.1)],
        'D': [('A', 1.4), ('F', 2.7), ('G', 2.4)],
        'E': [('B', 1.4), ('C', 1.8), ('F', 1.4), ('H', 1.6)],
        'F': [('C', 2.1), ('D', 2.7), ('E', 2.4), ('G', 1.3), ('H', 1.2)],
        'G': [('D', 2.4), ('F', 1.4), ('H', 1.5)],
        'H': [('E', 1.6), ('F', 1.2), ('G', 1.5)],
        }
    distances = dijkstra(graph, 'A')
    print(distances)
