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
        dist = {vertex: 0 for vertex in self.vertices}
        dist[start] = 10**9

        while True:
            if not (False in visited.values()):
                break
            candidates = {}
            for vertex in visited:
                if not visited[vertex]:
                    candidates[vertex] = dist[vertex]
            max_vertex = max(candidates, key=candidates.get)
            visited[max_vertex] = True

            for neighbor in self.graph[max_vertex]:
                new_dist = max(min(dist[max_vertex], neighbor[1]),
                               dist[neighbor[0]])
                dist[neighbor[0]] = new_dist
        return dist


graph_1 = Graph()
graph_1.add_edge(1, 2, 50)
graph_1.add_edge(2, 3, 60)
graph_1.add_edge(1, 3, 30)

print(graph_1.graph)
print(graph_1.dijkstra(1))
