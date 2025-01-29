# ハフマンコードを作成する際に用いる木を描画するシステム
# Jupyter環境での使用を推奨: (!pip install graphviz)
# 使用するためにはPCにGraphvizのインストールが必須である
# 数行下のパスは個人で指定する
# 
# 使い方:
# 下の方にある frequencies の中にそれぞれの確率を少数で書き込む
import heapq
from collections import defaultdict
from graphviz import Digraph
import os


# Graphvizのインストールディレクトリを指定
os.environ["PATH"] += os.pathsep + r'C:\Program Files\Graphviz\bin'

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def generate_codes(node, prefix="", codebook={}):
    if node is not None:
        if node.char is not None:
            codebook[node.char] = prefix
        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)
    return codebook

def visualize_huffman_tree(node, graph=None):
    if graph is None:
        graph = Digraph()

    if node.char is not None:
        graph.node(str(id(node)), label=f"{node.char}:{node.freq}")
    else:
        graph.node(str(id(node)), label=str(node.freq))

    if node.left is not None:
        graph.edge(str(id(node)), str(id(node.left)), label="0")
        visualize_huffman_tree(node.left, graph)

    if node.right is not None:
        graph.edge(str(id(node)), str(id(node.right)), label="1")
        visualize_huffman_tree(node.right, graph)

    return graph

frequencies = {
    'A': 0.15,
    'G': 0.25,
    'C': 0.20,
    'T': 0.40,
}

huffman_tree = build_huffman_tree(frequencies)
codes = generate_codes(huffman_tree)

tree_graph = visualize_huffman_tree(huffman_tree)
tree_graph.render('huffman_tree', view=True, format='png')