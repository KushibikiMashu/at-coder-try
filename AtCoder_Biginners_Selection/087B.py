def solve():
    x, y, z, n = [int(input()) for _ in range(4)]
    ans = 0
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if 500 * i + 100 * j + 50 * k == n:
                    ans += 1
    return ans

print(solve())
