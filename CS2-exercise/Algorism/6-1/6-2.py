from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self): 
        return str(self.value)

def print_bfs(top):
    if top is None:
        return

    queue = deque([top])
    result = []
    while queue:
        current_node = queue.popleft()
        result.append(current_node.value)
        if current_node.left:
            queue1.append(current_node.left)
        if current_node.right:
            queue1.append(current_node.right)

    print(", ".join(map(str, result)))


top = Node(1)
top.left = Node(2)
top.right = Node(3)
top.left.left = Node(4)
top.left.right = Node(5)
top.right.left = Node(6)
top.right.right = Node(7)

print_bfs(top)