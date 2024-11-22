import heapq
nodes = 7 # 頂点数
connect = [[] for _ in range(nodes)]

# [ グラフの設定 ]
# *1 = 辺の始点, *2 = 辺の終点, *3 = 辺の重み
#      *1         *2 *3
connect[0].append((1, 2))
connect[0].append((2, 8))
connect[0].append((3, 4))
connect[1].append((4, 3))
connect[2].append((4, 2))
connect[2].append((5, 3))
connect[3].append((5, 8))
connect[4].append((6, 9))
connect[5].append((6, 3))

def dijkstra(s, g):
    decideList = []
    dist = [-1] * nodes
    route = [-1] * nodes
    que = []
    heapq.heappush(que, (0, s, -1))
    now = s
    while len(que):
        data = heapq.heappop(que)
        now, value, last = data[1], data[0], data[2]
        
        if dist[now] != -1:
            continue

        # decide
        dist[now] = value
        route[now] = last
        decideList.append(str(now))

        for next, tv in connect[now]:
            if dist[next] != -1:
                continue

            heapq.heappush(que, (value + tv, next, now))

    minroute = [str(g)]
    now = g
    while True:
        if route[now] == 0:
            minroute.append(str(s))

        else:
            minroute.append(str(route[now]))

        now = route[now]
        if now == 0:
            break

    print("<< {} からの最短距離 >>".format(s))
    print(", ".join(list(map(str, dist))))
    print("* たどり着くことができない頂点は -1 と表示されます")
    print("<< {} → {} の最短経路 >>".format(s, g))
    print(", ".join(minroute[::-1]))
    print("<< 最短距離の確定順 >>")
    print(", ".join(decideList))

dijkstra(0, 6)