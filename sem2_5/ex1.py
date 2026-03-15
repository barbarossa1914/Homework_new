from collections import defaultdict

n = int(input())
words = input().split()
m, l = list(map(int, input().split()))
table = list()
for i in range(m):
    row = input().split()
    table.append(row)


class Graph:

    def __init__(self):
        self.vertices = set()
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.vertices.add(u)
        self.vertices.add(v)
        self.graph[u].append(v)

    def dfs(self, start, w, step=0, visited=None):
        if visited is None:
            visited = {vertex: False for vertex in self.vertices}

        visited[start] = True

        if step == len(w) - 1:
            return True

        for neighbor in self.graph[start]:
            if neighbor[0] == w[step + 1] and not visited[neighbor]:
                if self.dfs(neighbor, w, step + 1, visited):
                    return True

        visited[start] = False
        return False


gr = Graph()

for i in range(m):
    for j in range(l):
        els = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
        for el in els:
            if el[0] >= 0 and el[0] < m and el[1] >= 0 and el[1] < l:
                gr.add_edge((table[i][j], (i,j)), (table[el[0]][el[1]], el))

ans = []
flag = 0
for word in words:
    for i in range(m):
        if flag:
            break
        for j in range(l):
            first_letter = table[i][j]
            if first_letter == word[0]:
                state = gr.dfs((word[0], (i, j)), word)
                if state:
                    ans.append(word)
                    flag = 1
                    break
    flag = 0

print(ans)

