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
        dist = {vertex: 10 ** 9 for vertex in self.vertices}
        prev = {vertex: None for vertex in self.vertices}

        dist[start] = 0

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
                new_dist = dist[min_vertex] + neighbor[1]
                if new_dist < dist[neighbor[0]]:
                    dist[neighbor[0]] = new_dist
                    prev[neighbor[0]] = min_vertex

        return dist, prev


def get_path(prev, start, end):
    path = []
    current = end

    if prev[current] is None and current != start:
        return None

    while current is not None:
        path.append(current)
        current = prev[current]

    path.reverse()
    return path


v, e, start, end = input().split()
graph_1 = Graph()

for i in range(int(e)):
    s1, s2, time = input().split()
    graph_1.add_edge(s1, s2, int(time))

dist, prev = graph_1.dijkstra(start)

path = get_path(prev, start, end)
path = ' -> '.join(path)

with open('path.txt', 'w') as path_file:
    path_file.write(path)
