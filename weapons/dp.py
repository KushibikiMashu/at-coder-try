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
