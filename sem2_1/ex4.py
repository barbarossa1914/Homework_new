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
graph_keys = set(graph.keys())

color = {key: 'white' for key in graph_keys}

flag = False


def dfs(g, start, parent=None):
    global flag
    color[start] = 'grey'

    for el in g[start]:
        if el != parent and color[el] == 'grey':
            flag = True
        if color[el] == 'white':
            dfs(g, el, start)

    color[start] = 'black'


for key in graph_keys:
    if color[key] == 'white':
        dfs(graph, key)
    if flag:
        break

print(flag)
