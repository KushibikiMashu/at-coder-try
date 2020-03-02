# DPは漸化式

# 貰うDP
# 問題 https://atcoder.jp/contests/dp/tasks/dp_a
# 解法 https://qiita.com/drken/items/dc53c683d6de8aeacf5a#%E8%A7%A3%E6%B3%95
N = int(input())
A = list(map(int, input().split()))

INF = 10 ** 9
dp = [INF] * (N+1)
dp[0] = 0

for i in range(1, N):
    c1 = abs(A[i]-A[i-1])
    dp[i] = min(dp[i], dp[i-1] + c1)

    if i > 1:
        c2 = abs(A[i]-A[i-2])
        dp[i] = min(dp[i], dp[i-2] + c2)

return dp[N-1]

# ナップザック問題
# 入力を受け取る
N, W = map(int, input().split())
value = [0] * (N + 1)
weight = [0] * (N + 1)
for i in range(N):
    a, b = list(map(int, input().split()))
    value[i] = a
    weight[i] = b

# dpテーブルの初期化
dp = [[-float('inf') for i in range(W + 1)] for i in range(N + 10)]
for w in range(W+1):
    dp[0][w] = 0

for i in range(N+1):
    for j in range(W + 1):
        if j - weight[i] < 0:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(dp[i][j], dp[i][j - weight[i]] + value[i])

return max(dp[N])
