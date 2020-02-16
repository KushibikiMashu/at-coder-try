def solve():
    n, mi, ma = list(map(int, input().split()))
    ans = 0
    for i in range(1, n+1):
        s = sum(list(map(int, str(i))))
        if mi <= s <= ma:
            ans += i
    return ans

print(solve())
