# BFS
from collections import deque
nodes = 6 # 頂点数
s = 0 # 始点の座標
connect = [[] for _ in range(nodes+1)]
# [ グラフの設定 ]
# *1 = 辺の始点, *2 = 辺の終点
#      *1    *2
connect[0] = [1, 5]
connect[1] = [3, 5]
connect[2] = [1]
connect[3] = [2, 4]
connect[4] = []
connect[5] = [4]

#a = 0, b = 1, c = 2, d = 3, e = 4, f = 5

que = deque()
que.append(s)
visited = [False] * (nodes + 1)
route = [s]
while len(que):
    now = que.popleft()
    for next in connect[now]:
        if not visited[next]:
            route.append(next)
            visited[next] = True
            que.append(next)

print("<< 探索順(幅優先探索 / BFS) >>")
print(", ".join(list(map(str, route))))