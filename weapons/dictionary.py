# pythonにおけるmap

# keys
dic = {"A": "cat", "B": "dog"}
k = dic.keys()
print(k)
# 出力
# ["A", "B"]

# values
v = dic.values()
print(v)
# ["cat", "dog"]

#
dic = {"A": "cat", "B": "dog"}
i = dic.items()
print(i)
# dict_items([('A', 'cat'), ('B', 'dog')])

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
