from collections import defaultdict


class Graph:

    def __init__(self):
        self.vertices = set()
        self.graph = defaultdict(list)

    def add_edge(self, u, v, cost):
        self.vertices.add(u)
        self.vertices.add(v)
        self.graph[u].append((v, cost))

    def dijkstra(self, start, end):
        distance = {vertex: 10 ** 9 for vertex in self.vertices}
        visited = {vertex: False for vertex in self.vertices}
        distance[start] = 0

        while True:
            if not (False in visited.values()):
                break
            candidates = {}
            for vertex in visited:
                if not visited[vertex]:
                    candidates[vertex] = distance[vertex]
            min_vertex = min(candidates, key=candidates.get)
            visited[min_vertex] = True

            for neighbor in self.graph[min_vertex]:
                new_dist = max(distance[min_vertex], neighbor[1])
                distance[neighbor[0]] = new_dist
        return distance[end]


graph_1 = Graph()
n = int(input())
start_vertex = tuple(map(int, input().split()))
end_vertex = tuple(map(int, input().split()))
arr = list()
arr.append(start_vertex)
arr.append(end_vertex)

for i in range(n - 2):
    arr.append(tuple(map(int, input().split())))

for el_1 in arr:
    for el_2 in arr:
        if el_1 != el_2:
            c = ((el_1[0] - el_2[0]) ** 2 + (el_1[1] - el_2[1]) ** 2) ** 0.5
            graph_1.add_edge(el_1, el_2, c)

ans = graph_1.dijkstra(start_vertex, end_vertex)
print(round(ans, 3))
