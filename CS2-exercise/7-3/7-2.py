import networkx as nx

# グラフの定義
graph = nx.DiGraph()
edges = [('a', 'b', 1), ('a', 'd', 3), ('a', 'c', 2),
        ('b', 'a', 10), ('b', 'e', 3),
        ('c', 'f', 2),
        ('d', 'e', 2), ('d', 'f', 5),  # d -> f コスト修正済
        ('e', 'b', 3),
        ('f', 'e', 1)]
graph.add_weighted_edges_from(edges)


# ダイクストラ法の関数
def dijkstra(graph, start_node):
    distances = {node: float('inf') for node in graph.nodes}
    distances[start_node] = 0
    visited = set()
    unvisited = set(graph.nodes)

    while unvisited:
        current_node = min(unvisited, key=lambda node: distances[node], default=None)
        if current_node is None:
            break  # 全てのノードが到達不可能な場合

        unvisited.remove(current_node)
        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            new_distance = distances[current_node] + weight['weight']
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

    return distances


# 最短経路計算の実行 (ダイクストラ法)
start_node = 'a'
distances = dijkstra(graph, start_node)

# 最短経路計算の実行 (NetworkX)
nx_shortest_paths = {}
for node in graph.nodes:
    try:
        nx_shortest_paths[node] = nx.shortest_path_length(graph, source=start_node, target=node, weight='weight')
    except nx.NetworkXNoPath:
        nx_shortest_paths[node] = float('inf') # 経路が存在しない場合は無限大


# 結果出力 (必要に応じてコメントアウトを外して確認)
#print("ダイクストラ法:", distances)
#print("NetworkX:", nx_shortest_paths)