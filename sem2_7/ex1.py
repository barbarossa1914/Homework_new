from collections import defaultdict


class FlowNetwork:

    def __init__(self):
        self.vertices = set()
        self.graph = defaultdict(list)
        self.capacity = {}
        self.flow = {}

    def add_edge(self, u, v, cap=0):
        self.vertices.add(u)
        self.vertices.add(v)
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.capacity[(u, v)] = cap
        self.capacity[(v, u)] = cap
        self.flow[(u, v)] = 0
        self.flow[(v, u)] = 0

    def dfs(self, start, end, visited=None, path=None, min_capacity=float('inf')):
        if visited is None:
            visited = {vertex: False for vertex in self.vertices}
        if path is None:
            path = []

        visited[start] = True
        path.append(start)

        if start == end:
            return path, min_capacity

        for neighbor in self.graph[start]:
            if not visited[neighbor] and self.capacity[(start, neighbor)] > 0:
                new_min = min(min_capacity, self.capacity[(start, neighbor)])
                result = self.dfs(neighbor, end, visited, path, new_min)
                if result[0] is not None:
                    return result

        path.pop()
        return None, 0

    def ford_fulkerson(self, s, t):
        for vertex in self.vertices:
            for neighbor in self.graph[vertex]:
                self.flow[(vertex, neighbor)] = 0

        sum_flow = 0

        path, min_flow = self.dfs(s,t)
        while path != None:
            for i in range(len(path) - 1):
                self.flow[(path[i], path[i + 1])] += min_flow
                self.capacity[(path[i], path[i + 1])] -= min_flow
                self.flow[(path[i + 1], path[i])] -= min_flow
                self.capacity[(path[i + 1], path[i])] += min_flow
            sum_flow += min_flow
            path, min_flow = self.dfs(s, t)

        return sum_flow

ans = []
flag = 1
n = int(input())
while flag:
    fl = FlowNetwork()
    s, t, c = list(map(int, input().split()))
    for i in range(c):
        a, b, w = list(map(int, input().split()))
        fl.add_edge(a, b, w)
    ans.append(fl.ford_fulkerson(s, t))
    if int(input()) == 0:
        flag = 0

print(ans)


