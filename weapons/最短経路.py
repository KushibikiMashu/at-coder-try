# ---
# ベルマン・フォード法
# 計算量はO(V * E)
# 二点間
# ---

# 入力
# 7 10
# 1 2 2
# 1 3 5
# 3 2 4
# 3 4 2
# 2 5 10
# 2 4 6
# 4 6 1
# 6 7 9
# 5 6 3
# 5 7 5

def solve():
    V, E = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(E)]

    def has_negative_loop():
        d = [0 for _ in range(V)]

        for i in range(V):
            for j in range(E):
                e = A[i]
                f, t, c = e[0]-1, e[1]-1, e[2]
                if d[t] > d[f] + c:
                    if i == V-1:
                        return True

        return False

    def shortest_path(s):
        INF = 10 ** 5
        d = [INF for _ in range(V)]
        d[s] = 0

        while True:
            update = False
            for i in range(E):
                e = A[i]
                f, t, c = e[0]-1, e[1]-1, e[2]
                if d[f] != INF and d[t] > d[f] + c:
                    d[t] = d[f] + c
                    update = True
                # 無向グラフなので、from toを入れ替える
                # TODO これ本当に必要？
#                 if d[t] != INF and d[f] > d[t] + c:
#                     d[f] = d[t] + c
#                     update = True

            if not update: break
        return d

    ans = shortest_path(0)
    return ans[V-1]

# 0からの最小コストは
# [0, 2, 5, 7, 11, 8, 16]
print(solve()) # 16

# ---
# ダイクストラ法
# 負の辺がある場合は使えない
# 計算量はO(E * log(V))
# 二点間
# ---
# https://juppy.hatenablog.com/entry/2018/11/01/%E8%9F%BB%E6%9C%AC_python_%E5%8D%98%E4%B8%80%E6%9C%80%E7%9F%AD%E7%B5%8C%E8%B7%AF%E6%B3%952%EF%BC%88%E3%83%80%E3%82%A4%E3%82%AF%E3%82%B9%E3%83%88%E3%83%A9%E6%B3%95%EF%BC%89_%E7%AB%B6%E6%8A%80%E3%83%97

# https://juppy.hatenablog.com/entry/2019/02/18/%E8%9F%BB%E6%9C%AC_python_%E3%83%97%E3%83%A9%E3%82%A4%E3%82%AA%E3%83%AA%E3%83%86%E3%82%A3%E3%82%AD%E3%83%A5%E3%83%BC%28heapq%29%E3%82%92%E7%94%A8%E3%81%84%E3%81%9F%E3%83%97%E3%83%AA%E3%83%A0%E6%B3%95

from collections import deque, defaultdict

def solve():
    V, E = map(int, input().split())
    G = [[] for _ in range(V)]
    for _ in range(E):
        a, b, c = map(int, input().split())
        # 隣接リスト表現
        G[a-1].append([b-1, c])

    INF = 10 ** 5
    d = [INF for _ in range(V)]

    # sがstartの頂点
    def dijkstra(s):
        # スタート地点のコストを0にする
        d[s] = 0
        # (頂点, 最短距離)
        q = deque([(s, 0)])

        while q:
            p = q.popleft()
            v = p[0]
            if d[v] < p[1]: continue
            for i in range(len(G[v])):
                to, cost = G[v][i]
                if d[to] > d[v] + cost:
                    # 最小コストを更新する
                    d[to] = d[v] + cost
                    q.append((to, d[to]))
        return d

    ans = dijkstra(0)
    return ans[6]

print(solve()) # 17

# ---
# ワーシャル・フロイド法
# 負の辺がない場合を考える
# 計算量はO(V^3)
# 全点対最小経路
# dp
# ---

def solve():
    V, E = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(E)]

    INF = 10 ** 5
    d = [[INF]*V for _ in range(V)]

    for a, b, c in A:
        d[a-1][b-1] = c
        d[b-1][a-1] = c

    for i in range(V):
        d[i][i] = 0

    for k in range(V):
        for i in range(V):
            for j in range(V):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    for a in d:
        print(a)

    # start = 0, end = 6
    # ans = 16
    return d[0][6]

print(solve())

# 隣接行列表現
# before
# [0, 2, 5, 100000, 100000, 100000, 100000]
# [2, 0, 4, 6, 10, 100000, 100000]
# [5, 4, 0, 2, 100000, 100000, 100000]
# [100000, 6, 2, 0, 100000, 1, 100000]
# [100000, 10, 100000, 100000, 0, 3, 5]
# [100000, 100000, 100000, 1, 3, 0, 9]
# [100000, 100000, 100000, 100000, 5, 9, 0]

# after
# [0, 2, 5, 7, 11, 8, 16]
# [2, 0, 4, 6, 10, 7, 15]
# [5, 4, 0, 2, 6, 3, 11]
# [7, 6, 2, 0, 4, 1, 9]
# [11, 10, 6, 4, 0, 3, 5]
# [8, 7, 3, 1, 3, 0, 8]
# [16, 15, 11, 9, 5, 8, 0]

# d[i][i]が負の数なら、負の閉路がある
