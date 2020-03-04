# parant, rankの初期化
n = 10
parent = [i for i in range(n)]
rank = [0] * n

# 木の根(root)を求める
# 親を求める
def find(x):
    if parent[x] == x:
        return x
    else:
        # keyとvalueが同じ位置に当たるまで親をたどる
        parent[x] = find(parent[x])
        return parent[x]

# 併合
def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y: return

    if rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1
            return rank[x]

# 同じグループか判定する
def isSame(x, y):
    return find(x) == find(y)
