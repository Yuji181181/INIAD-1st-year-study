
# NetworkX 使用ガイド

## 1. NetworkX の初期設定

```python
import networkx as nx
import matplotlib.pyplot as plt

# グラフの作成
G = nx.Graph()
2. ノードとエッジの追加ノードを追加するG.add_node(1)  # ノード1を追加
G.add_nodes_from([2, 3])  # 一括でノード2とノード3を追加
エッジを追加するG.add_edge(1, 2)  # ノード1とノード2の間にエッジを追加
G.add_edges_from([(1, 3), (2, 3)])  # ノード1と3、およびノード2と3の間にエッジを追加
3. 最短経路検索ダイクストラ法を用いた最短経路の検索# エッジに重みを設定
G.add_weighted_edges_from([(1, 2, 10), (1, 3, 5), (2, 3, 2)])

# 最短経路の計算
shortest_path = nx.shortest_path(G, source=1, target=2)
print("ノード1からノード2への最短経路:", shortest_path)
4. 重みづけエッジの重みを設定# 重み付きエッジの追加
G.add_edge(1, 2, weight=10)
G.add_edge(1, 3, weight=5)
G.add_edge(2, 3, weight=2)

#dfs
nx.dfs_edges(G, source=1)
#bfs
nx.bfs_edges(G, source=1)

# 重みの取得
weight = G[1][2]['weight']
print("ノード1とノード2の重み:", weight)
5. グラフの可視化Matplotlibを使用してグラフを描画pos = nx.spring_layout(G)  # ノードの位置を計算
nx.draw(G, pos, with_labels=True)
edge_labels = nx.get_edge_attributes(G, 'weight')  # 重みを取得
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)  # 重みをラベルとして表示
plt.show()
```
参考
NetworkX 公式ドキュメント