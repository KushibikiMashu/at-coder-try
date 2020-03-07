class UnionFind:
    parent = []
    rank = []

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def count(self, x):
        return self.parent.count(x)

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y: return

        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
                return self.rank[x]

    def isSame(self, x, y):
        return self.find(x) == self.find(y)

uf = UnionFind(10)

# parant, rankの初期化
n = 10
parent = [i for i in range(n)]
rank = [0] * n

# 木の根(root)を求める
# 親を求める
def find(x, parent):
    if parent[x] == x:
        return x
    else:
        # keyとvalueが同じ位置に当たるまで親をたどる
        parent[x] = find(parent[x], parent)
        return parent[x]

# 併合
def unite(x, y, parent):
    x = find(x, parent)
    y = find(y, parent)
    if x == y: return

    parent[y] = x

# 同じグループか判定する
def isSame(x, y, parent):
    return find(x, parent) == find(y, parent)

# ---
# rank有りのunite
# ---
def unite(x, y, parent):
    x = find(x, parent)
    y = find(y, parent)
    if x == y: return

    if rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1
            return rank[x]
