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
        distances = {vertex: 10**9 for vertex in self.vertices}
        previous = {vertex: -1 for vertex in self.vertices}
        distances[start] = 0

        while True:
            if not (False in visited.values()):
                break
            candidates = {}
            for vertex in visited:
                if not visited[vertex]:
                    candidates[vertex] = distances[vertex]
            min_vertex = min(candidates, key=candidates.get)
            visited[min_vertex] = True

            for neighbor in self.graph[min_vertex]:
                new_distance = distances[min_vertex] + neighbor[1]
                if new_distance < distances[neighbor[0]]:
                    distances[neighbor[0]] = new_distance
                    previous[neighbor[0]] = min_vertex

        return distances, previous


def get_prev(previous, ff):

    if not previous[ff]:
        return -1
    res = []
    while ff != -1:
        res.append(ff)
        ff = previous[ff]
    return res


graph_1 = Graph()

n, m, s, f = list(map(int, input().split()))
for i in range(m):
    v1, v2, c = list(map(int, input().split()))
    graph_1.add_edge(v1, v2, c)

min_dist, prev = graph_1.dijkstra(s)

print(min_dist[f], list(reversed(get_prev(prev, f))))
