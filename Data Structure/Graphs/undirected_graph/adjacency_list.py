from collections import defaultdict


class Graph:
    def __init__(self):
        # initializing the graph as dictionary of lists
        self.graph = defaultdict(list)

    def insert_edge(self, vertex1, vertex2):
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)  # same as directed just added this line undirected graph

    def show_graph(self):
        for vertex in self.graph:
            print(vertex, "=>", self.graph[vertex])


graph = Graph()
graph.insert_edge(1, 5)
graph.insert_edge(1, 10)
graph.insert_edge(3, 1)
graph.insert_edge(5, 3)
graph.insert_edge(5, 10)
graph.insert_edge(10, 3)

graph.show_graph()
