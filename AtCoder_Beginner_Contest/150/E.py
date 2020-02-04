MOD = 10 ** 9 + 7

def solve(N, A):
    A.sort()
    two = [0] * (N + 1)
    for i in range(N + 1):
        two[i] = 2 ** i

    ans = 0
    for i in range(N):
        l = i
        r = N-i-1
        now = two[r]
        if r != 0:
            now += two[r-1] * r
        now *= two[l]
        now *= A[i]
        ans += now

    ans *= two[N]

    return ans % MOD

    return 0

N = int(input())
A = list(map(int, input().split()))

print(solve(N, A))

# n = int(input())
# ccc = list(map(int, input().split()))
# ccc.sort()
# MOD = 10 ** 9 + 7
# ans = 0
# others = pow(4, n - 1, MOD)
# for i, c in enumerate(ccc):
#     ans = (ans + others * c * (n - i + 1)) % MOD
# print(ans)
