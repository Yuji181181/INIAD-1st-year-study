"""
二分探索木の操作とトラバースを確認するためのツール

使用方法:
1. このファイルを実行すると、以下の操作が順に実行されます：
   - 初期値[12, 5, 2, 7, 15, 13, 20]で二分探索木を構築
   - 3を追加
   - 100を追加
   - 20を削除
   - 10を削除（存在しない要素の削除テスト）

2. 最終的な木構造に対して以下の3種類のトラバースを実行し、結果を表示します：
   - 行きがけ順（pre-order）: ルート → 左 → 右
   - 通りがけ順（in-order）: 左 → ルート → 右
   - 帰りがけ順（post-order）: 左 → 右 → ルート

3. カスタマイズ:
   - initial_values リストを変更することで、異なる初期値で開始できます
   - プログラム末尾の操作を追加・変更することで、異なる操作を試すことができます
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._add_rec(self.root, value)

    def _add_rec(self, node, value):
        if value < node.value:
            if node.left:
                self._add_rec(node.left, value)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self._add_rec(node.right, value)
            else:
                node.right = Node(value)

    def remove(self, value):
        self.root = self._remove_rec(self.root, value)

    def _remove_rec(self, node, value):
        if not node:
            return None

        if value < node.value:
            node.left = self._remove_rec(node.left, value)
        elif value > node.value:
            node.right = self._remove_rec(node.right, value)
        else:
            # 削除対象ノードが見つかった場合
            if not node.left:
                return node.right  # 左の子がない場合は右の子を接続
            elif not node.right:
                return node.left  # 右の子がない場合は左の子を接続

            # 左右に子がいる場合は右部分木の最小値を取得して置き換える
            min_value = self._find_min(node.right)
            node.value = min_value
            node.right = self._remove_rec(node.right, min_value)

        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node.value

    def pre_order_traversal(self):
        """行きがけ順 (ルート -> 左 -> 右)"""
        result = []
        self._pre_order_rec(self.root, result)
        return result

    def _pre_order_rec(self, node, result):
        if node:
            result.append(node.value)  # ルートを最初に追加
            self._pre_order_rec(node.left, result)  # 左の子ノードを探索
            self._pre_order_rec(node.right, result)  # 右の子ノードを探索

    def in_order_traversal(self):
        """通り掛け順 (左 -> ルート -> 右)"""
        result = []
        self._in_order_rec(self.root, result)
        return result

    def _in_order_rec(self, node, result):
        if node:
            self._in_order_rec(node.left, result)  # 左の子ノードを探索
            result.append(node.value)  # ルートを追加
            self._in_order_rec(node.right, result)  # 右の子ノードを探索

    def post_order_traversal(self):
        """帰りがけ順 (左 -> 右 -> ルート)"""
        result = []
        self._post_order_rec(self.root, result)
        return result

    def _post_order_rec(self, node, result):
        if node:
            self._post_order_rec(node.left, result)  # 左の子ノードを探索
            self._post_order_rec(node.right, result)  # 右の子ノードを探索
            result.append(node.value)  # ルートを最後に追加


# 初期状態のBSTを構築する
bst = BinarySearchTree()
initial_values = [12, 5, 2, 7, 15, 13, 20]  # 最初のデータを修正
for value in initial_values:
    bst.add(value)

# 操作を順に実行
bst.add(3)  # 3を追加
bst.add(100)  # 100を追加
bst.remove(20)  # 20を削除
bst.remove(10)  # 10を削除

# 各トラバースの結果を取得
pre_order_result = bst.pre_order_traversal()  # 行きがけ順
in_order_result = bst.in_order_traversal()  # 通り掛け順
post_order_result = bst.post_order_traversal()  # 帰りがけ順

# 結果を表示
print("行きがけ順:", pre_order_result)
print("通り掛け順:", in_order_result)
print("帰りがけ順:", post_order_result)
