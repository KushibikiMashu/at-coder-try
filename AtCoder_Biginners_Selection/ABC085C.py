def solve():
    N, M = map(int, input().split())
    l = [-1, -1, -1]
    for i in range(N+1):
        for j in range(N-i+1):
            if 1000 * i + 5000 * j + 10000 * (N-i-j) == M:
                l = [i, j, N-i-j]
    print(l[2], l[1], l[0])

print(solve())
