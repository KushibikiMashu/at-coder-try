# import math
# import numpy as np

# S = input()
# N = int(input())
N, W = map(int, input().split())
# A = list(map(int, input().split()))
# B = [int(input()) for _ in range(n)]
A = []
B = []
for _ in range(N):
    a, b = list(map(int, input().split()))
    A.append(a)
    B.append(b)
# As = np.array(As)
# Bs = np.array(Bs)

# 二次元配列の初期化
# [[inf, inf, inf], [inf, inf, inf]]
dp = [[0] * (W + 1) for i in range(N + 1)]

def solve():
    for i in range(N):
        for w in range(W + 1):
            if w - A[i] >= 0:
                dp[i+1][w] = max(dp[i+1][w], dp[i][w - A[i]] + B[i])

            dp[i+1][w] = max(dp[i+1][w], dp[i][w])

    return dp[N][W]

# 0 [0, 0, 0, 0, 0, 0, 0, 0, 0]
# 1 [0, 0, 0, 30, 30, 30, 30, 30, 30]
# 2 [0, 0, 0, 30, 50, 50, 50, 80, 80]
# 3 [0, 0, 0, 30, 50, 60, 60, 80, 90]

print(solve())
