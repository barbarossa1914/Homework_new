n = int(input())
graph = dict()

for i in range(n):
    string = list(map(int, input().split()))
    if string[0] not in graph:
        graph[string[0]] = [string[1]]
    else:
        graph[string[0]].append(string[1])
    if string[1] not in graph:
        graph[string[1]] = [string[0]]
    else:
        graph[string[1]].append(string[0])
graph_values = set(graph.keys())


def bfs(g, start):
    queue = []
    visited = set()

    queue.append(start)
    visited.add(start)

    while queue:
        node = queue.pop(0)
        for neighbor in g[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    if visited == graph_values:
        return 1
    else:
        return 0


ans = 'True'
for key in graph.keys():
    if bfs(graph, key) == 0:
        ans = 'False'
        break
print(ans)
