from collections import defaultdict


class Graph:

    def __init__(self):
        self.vertices = set()
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.vertices.add(u)
        self.vertices.add(v)
        self.graph[u].append(v)

    def dfs(self, start, visited, step):
        visited[start] = step
        if (step + 1) % 2:
            step = 1
        else:
            step = 2

        for neighbor in self.graph[start]:
            if not visited[neighbor]:
                visited[neighbor] = step
                res = self.dfs(neighbor, visited, step)
                if res == 'NO':
                    return 'NO'
            else:
                if visited[neighbor] == visited[start]:
                    return 'NO'

        return 'YES'

    def check_bipartite(self):
        for vertex in self.vertices:
            visited = {vertex: 0 for vertex in gr.vertices}
            if self.dfs(vertex, visited, 1) == 'NO':
                return 'NO'
        return 'YES'


gr = Graph()

with open('input.txt', 'r') as file:
    n, m = list(map(int, file.readline().split()))
    for i in range(m):
        u, v = list(map(int, file.readline().split()))
        gr.add_edge(u, v)

ans = gr.check_bipartite()

with open('output.txt', 'w') as file:
    file.write(ans)
