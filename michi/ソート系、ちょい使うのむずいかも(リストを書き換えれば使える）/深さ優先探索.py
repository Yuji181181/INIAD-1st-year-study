# DFS
nodes = 6 # 頂点数
s = 0 # 始点の座標
connect = [[] for _ in range(nodes+1)]
# [ グラフの設定 ]
# *1 = 辺の始点, *2 = 辺の終点
#      *1    *2
connect[0] = [1, 2, 3]
connect[1] = [2, 5]
connect[2] = [5]
connect[3] = [2]
connect[4] = [2, 3]
connect[5] = [4]

def dfs(now, visited):
    global route
    for next in connect[now]:
        if next not in visited:
            visited.add(next)
            route.append(next)
            dfs(next, visited)

route = [s]
dfs(s, set([s]))
print("<< 探索順(深さ優先探索 / DFS) >>")
print(", ".join(list(map(str, route))))