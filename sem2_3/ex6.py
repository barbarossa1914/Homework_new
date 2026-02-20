from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)

    def transpose(self):
        graph_transposed = Graph()
        for u in self.vertices:
            for v in self.graph[u]:
                graph_transposed.add_edge(v, u)
        return graph_transposed

    def dfs_first(self, start_vertex, visited, finishing_time):
        visited[start_vertex] = True

        for vertex in self.graph[start_vertex]:
            if not visited[vertex]:
                self.dfs_first(vertex, visited, finishing_time)

        finishing_time.append(start_vertex)

    def dfs_second(self, start_vertex, visited, scc):
        visited[start_vertex] = True
        scc.append(start_vertex)

        for vertex in self.graph[start_vertex]:
            if not visited[vertex]:
                self.dfs_second(vertex, visited, scc)

    def find_sccs(self):
        visited = {vertex: False for vertex in self.vertices}
        finishing_time = []

        for vertex in self.vertices:
            if not visited[vertex]:
                self.dfs_first(vertex, visited, finishing_time)

        transposed_graph = self.transpose()

        visited = {vertex: False for vertex in self.vertices}
        sccs = []

        for vertex in reversed(finishing_time):
            if not visited[vertex]:
                current_scc = []
                transposed_graph.dfs_second(vertex, visited, current_scc)
                sccs.append(current_scc)

        return sccs


n = int(input())
m = int(input())

graph1 = Graph()
for i in range(m):
    v1, v2 = list(map(int, input().split()))
    graph1.add_edge(v1, v2)

print(len(graph1.find_sccs()))