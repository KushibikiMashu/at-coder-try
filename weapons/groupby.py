from itertools import groupby

binaries = [0,0,0,1,1,0,0,0,1,1,0,1]
gr = groupby(binaries)
for key, group in gr:
    print(f'{key}: {list(group)}')

# 0: [0, 0, 0]
# 1: [1, 1]
# 0: [0, 0, 0]
# 1: [1, 1]
# 0: [0]
# 1: [1]

# -------------------

# ソートするといい
from itertools import groupby

binaries = [0,0,0,1,1,0,0,0,1,1,0,1]
binaries.sort()
gr = groupby(binaries)
for key, group in gr:
    print(f'{key}: {list(group)}')

# 0: [0, 0, 0, 0, 0, 0, 0]
# 1: [1, 1, 1, 1, 1]

# -------------------

# 隣接リストを作る
# input
# 1 2
# 1 3
# 2 3

A = [[1,2], [1, 3], [2, 3]]
d = {}
for a, b in A:
    d.setdefault(a, []).append(b)

print(V) # {1: [2, 3], 2: [3]}

for k, v in d.items():
    print(k, v)

# 1 [2, 3]
# 2 [3]

# -------------------

# 同じものの個数を数える。map（辞書）の性質を利用する
from collections import defaultdict

binaries = [0,0,0,1,1,0,0,0,1,1,0,1]
d = defaultdict(int)
for b in binaries:
    d[b] += 1

# 辞書型
print(d) #  defaultdict(<class 'int'>, {0: 7, 1: 5})

# key => value（タプル）の配列
l = list(d.items())
print(l) # [(0, 7), (1, 5)]
