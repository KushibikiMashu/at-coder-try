def solve():
    N = int(input())
    B = [int(input()) for _ in range(N)]
    return len(set(B))

print(solve())
