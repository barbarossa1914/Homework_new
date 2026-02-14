from collections import defaultdict

nn = int(input())
x, y = list(map(int, input().split()))
x, y = x - 1, y - 1
start_cell = (x, y)
chessboard = [[0 for i in range(nn)] for j in range(nn)]

class Graph:

    def __init__(self):
        self.vertices = set()
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)

    def dfs(self, start_vertex, visited):
        visited[start_vertex] = True

        for vertex in self.graph[start_vertex]:
            if not visited[vertex]:
                self.dfs(vertex, visited)

    def bfs(self, start):
        visited = set()
        queue = []
        dist = {v: 10**9 for v in self.vertices}
        queue.append(start)
        visited.add(start)
        dist[start] = 0

        while queue:
            v = queue.pop(0)
            for u in self.graph[v]:
                if dist[u] == 10**9:
                    dist[u] = dist[v] + 1
                    queue.append(u)
        return dist


graph_1 = Graph()

def build_graph(n, start_x, start_y, board, graph):
    board[start_x][start_y] = 1
    moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
    for move in moves:
        h_x, h_y = move[0] + start_x, move[1] + start_y
        if (-1 < h_x < n) and (-1 < h_y < n):
            graph.add_edge((start_x, start_y), (h_x, h_y))
            graph.add_edge((h_x, h_y), (start_x, start_y))
            if not board[h_x][h_y]:
                build_graph(n, h_x, h_y, board, graph)


build_graph(nn, x, y, chessboard, graph_1)
print(graph_1.graph)
print(graph_1.bfs(start_cell))

