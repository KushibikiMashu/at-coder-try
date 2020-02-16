def solve():
    A = list(map(int, input().split()))

    ans = 0
    for i in range(1, A[0]+1):
        s = sum(list(map(int, str(i))))
        if A[1] <= s <= A[2]:
            ans += i
    return ans

print(solve())
