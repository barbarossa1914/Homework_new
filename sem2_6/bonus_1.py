import networkx as nx

G = nx.Graph()
G.add_edge(1, 2, weight=1)
G.add_edge(2, 3, weight=2)
G.add_edge(3, 4, weight=3)
G.add_edge(12, 13, weight=3)
for i in range(4, 11):
    G.add_edge(i, i - 1, weight=i ** 2)
    G.add_edge(i, i - 2, weight=i ** 2)
    G.add_edge(i, i - 3, weight=i ** 2)

largest_cc = max(nx.connected_components(G), key=len)
largest_subgraph = G.subgraph(largest_cc)
d = nx.diameter(largest_subgraph)
r = nx.radius(largest_subgraph)
paths = list(nx.all_pairs_shortest_path(G))

print(G.edges)
print(G.nodes)
print(d, r)
print(paths)
