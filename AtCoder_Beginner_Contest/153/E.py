# import math
# import numpy as np

# S = input()
# N = int(input())
H, N = map(int, input().split())
# A = list(map(int, input().split()))
# B = [int(input()) for _ in range(n)]
# A = []
# B = []
# for _ in range(N):
#     a, b = list(map(int, input().split()))
#     A.append(a)
#     B.append(b)

# 二次元配列
# [[inf, inf, inf], [inf, inf, inf]]
# dp = [[float('inf')] * (H + 1) for i in range(N + 1)]

INF = 10 ** 18
dp = [INF] * (H + 1)
dp[0] = 0

def solve():
    for i in range(N):
        a, b = list(map(int, input().split()))

        for j in range(H):
            nj = min(j + a, H)
            dp[nj] = min(dp[nj], dp[j] + b)
    return dp[H]

print(solve())
