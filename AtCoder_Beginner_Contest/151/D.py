from collections import deque

H, W = map(int, input().split())
field = [input() for _ in range(H)]
MOVE = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(h, w):
    # queueに(移動回数, (マスの縦のindex, マスの横のindex))という隣接するマスのデータを格納する
    q = deque([(0, (h, w))])
    visited = [[-1] * W for _ in range(H)]
    # l: 14からの破壊的代入により最大移動回数をメモする
    count = -1

    while q:
        count, (y, x) = q.popleft()
        # 訪問済みならskip
        if visited[y][x] != -1:
            continue
        # 訪問済みにする
        visited[y][x] = count

        for a, b in MOVE:
            next_x = x + a
            next_y = y + b
            # グリッドの外ならskip
            if next_x < 0 or next_x >= W or next_y < 0 or next_y >= H:
                continue
            # 訪問済みならskip
            if visited[next_y][next_x] != -1:
                continue
            # # 壁ならskip
            if field[next_y][next_x] == '#':
                continue
            q.append((count + 1, (next_y, next_x)))
    return count

def solve():
    ans = 0
    for h in range(H):
        for w in range(W):
            if field[h][w] == '#':
                continue
            count = dfs(h, w)
            ans = max(ans, count)
    return ans

print(solve())

