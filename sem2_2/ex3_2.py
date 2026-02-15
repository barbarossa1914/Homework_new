from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()

    def add_edge(self, u, v, cost):
        self.graph[u].append((v, cost))
        self.vertices.add(u)
        self.vertices.add(v)

    def dijkstra(self, start):
        visited = {vertex: False for vertex in self.vertices}
        dist = {vertex: 10**9 for vertex in self.vertices}
        dist[start] = 1

        while True:
            if not (False in visited.values()):
                break
            candidates = {}
            for vertex in visited:
                if not visited[vertex]:
                    candidates[vertex] = dist[vertex]
            min_vertex = min(candidates, key=candidates.get)
            visited[min_vertex] = True

            for neighbor in self.graph[min_vertex]:
                new_dist = min(dist[min_vertex]*neighbor[1],
                               dist[neighbor[0]])
                dist[neighbor[0]] = new_dist
        return dist


graph_1 = Graph()
graph_1.add_edge(1, 2, 10)
graph_1.add_edge(2, 3, 20)
graph_1.add_edge(1, 3, 100)

print(graph_1.graph)
print(graph_1.dijkstra(1))


