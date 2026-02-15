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
Graph_1 = Graph()
for i in range(n):
    s = list(map(int, input().split()))
    for el in s[1:]:
        Graph_1.add_edge(s[0], el)


def find_social_clusters():
    sccs_groups = Graph_1.find_sccs()
    sccs_groups.sort(key=lambda x: -len(x))
    for el in sccs_groups:
        el.sort()
    return sccs_groups


print(find_social_clusters())




