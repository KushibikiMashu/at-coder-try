N, M = map(int, input().split())
B = [list(input()) for _ in range(N)]
list = [['#']*M] * N

MOVE = [(0, 1),(0, -1),(1, 0),(-1, 0),(1, 1),(1, -1),(-1, 1),(-1, -1)]

for h in range(N):
    for w in range(M):
        count = 0

        for x, y in MOVE:
            next_h = h + y
            next_w = w + x
            if not 0 <= next_h < N or not 0 <= next_w < M:
                continue
            if B[next_h][next_w] == '#':
                count += 1

        list[h][w] = str(count)
        if B[h][w] == '#':
            list[h][w] = '#'

    print(''.join(list[h]))
