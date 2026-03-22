from collections import defaultdict


class Graph:
    def __init__(self):
        self.vertices = set()
        self.graph = defaultdict(list)
        self.match_to_cube = []
        self.match_to_pos = []
        self.result = []

    def add_edge(self, u, v):
        self.vertices.add(u)
        self.vertices.add(v)
        self.graph[u].append(v)
        self.graph[v].append(u)

    def build_graph(self, n, name, cubes):
        m = len(name)
        self.graph.clear()
        self.vertices.clear()

        for l in range(m):
            letter = name[l]
            for cube in range(n):
                if letter in cubes[cube]:
                    self.add_edge(l, cube + n)

        self.match_to_cube = [-1] * n
        self.match_to_pos = [-1] * m
        self.result = []

    def dfs(self, pos, visited, m, n):
        for cube in self.graph[pos]:
            if not visited[cube]:
                visited[cube] = True
                cube_id = cube - n

                if (self.match_to_cube[cube_id] == -1 or
                        self.dfs(self.match_to_cube[cube_id], visited, m, n)):
                    self.match_to_cube[cube_id] = pos
                    self.match_to_pos[pos] = cube_id
                    return True
        return False

    def find_perfect_matching(self, n, name, cubes):
        m = len(name)

        self.build_graph(n, name, cubes)

        for pos in range(m):
            visited = [False] * (m + n)
            if not self.dfs(pos, visited, m, n):
                return False

        self.result = [self.match_to_pos[pos] + 1 for pos in range(m)]
        return True


gr = Graph()
CUBES = []

with open('input.txt', 'r') as file:
    N = int(file.readline().strip())
    NAME = str(file.readline().strip())
    for i in range(N):
        CUBES.append(file.readline().strip().split())

ans = gr.find_perfect_matching(N, NAME, CUBES)
print(NAME)
with open('output.txt', 'w') as file:
    if ans:
        file.write('YES\n')
        file.write(''.join(list(map(str, gr.result))))
    else:
        file.write('NO')
