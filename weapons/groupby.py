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

print(d) # {1: [2, 3], 2: [3]}

for k, v in d.items():
    print(k, v)

# 1 [2, 3]
# 2 [3]
