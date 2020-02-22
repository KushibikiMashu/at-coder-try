from collections import deque

# [深さ優先探索]
#  訪問済みリストvisitedをfalseで初期化する
#  訪問予定リストのキューを初期化する
# 	キューから要素がなくなるまで、以下を繰り返す
# 	  キューから要素vを取り出す
# 	  その要素に隣接している頂点uを取得する（uに移動する）
# 	  uがもし訪問済み（visited[u] == true）であれば、
# 	    何もしない
# 	  (uが訪問済みでなければ、)
#       訪問済みリストの頂点uをtrueにする（uに移動する）
#       頂点uに隣接している頂点をキューに追加する

# input
# 8 7
# 3 7
# 2 7
# 1 2
# 1 6
# 5 6
# 4 5
# 4 8

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]

visited = [False] * N
visited[0] = True
d = {}
for a, b in A:
    d.setdefault(b-1, []).append(a-1)
    d.setdefault(a-1, []).append(b-1)

l = sorted(d.items())

print(l)
# [(0, [1, 5]), (1, [6, 0]), (2, [6]), (3, [4, 7]), (4, [5, 3]), (5, [0, 4]), (6, [2, 1]), (7, [3])]

def dfs(v, seen):
    if False not in seen: return 1

    c = 0
    for i in d[v]:
        if (seen[i]): continue
        seen[i] = True
        c += dfs(i, seen)
        seen[i] = False
    return c

print(dfs(0, visited))

