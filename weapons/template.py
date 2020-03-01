# import math
# import fractions
# import numpy as np

# ゼロ埋め
# l = [0] * N

def solve():
    # N = int(input())
    # N, M = map(int, input().split())
    # A = list(map(int, input().split()))
    # A = [int(input()) for _ in range(N)]

    return 0

# print(solve())

# テスト用
def resolve():
    print(solve())


# -----


# MOD = 10 ** 9 + 7

def solve():
    # S = input()
    # N = int(input())
    # B = [list(input()) for _ in range(N)] # グリッドグラフ用

    # 文字列をlistにする（'abc' -> ['a', 'b', 'c']）
    # L = list(input())

    # 1 2
    # N, M = map(int, input().split())

    # 1 2 3 4 5 6 7
    # A = list(map(int, input().split()))

    # M = 2
    # 1
    # 2
    # B = [int(input()) for _ in range(N)]

    # N = 3
    # 8 3
    # 4 2
    # 2 1
    # A = [list(map(int, input().split())) for _ in range(N)]
    # str
    # A = [list(input().split()) for _ in range(N)]

    # A = []
    # B = []
    # for _ in range(N):
    #     a, b = list(map(int, input().split()))
    #     A.append(a)
    #     B.append(b)
    # S = [tuple(map(int, input().split())) for _ in range(N)]
    # for (a, b) in S:
    #   do something

    return 0

# print(solve())

# テスト用
def resolve():
    print(solve())

# print
# intのリストを改行して出力
# see https://qiita.com/chiruno/items/21b65573bb696f4ce3ce
print('\n'.join(map(str, l)))

# 二次元配列
# [[inf, inf, inf], [inf, inf, inf]]
# dp = [[float('inf')] * (H + 1) for i in range(N + 1)]
# links = [set() for _ in range(N)]

# リストの要素に2を掛けたものを足す
# for文より高速
# sum = sum(a * 2 for a in A)

# 隣接行列表現。無向、重み付き
# 辺が少ないとメモリを無駄に消費してしまう。木の場合は 辺の数が|V|-1なので、隣接リストの方がベター
# 5
# 2 5 2
# 2 3 10
# 1 3 8
# 3 4 2
N = int(input())
A = [list(map(int, input().split())) for _ in range(N-1)]
g = [[0] * N for i in range(N)]

for v, u, w in A:
    g[v-1][u-1] = w
    g[u-1][v-1] = w

print(g)
