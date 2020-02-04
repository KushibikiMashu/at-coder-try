MOD = 10 ** 9 + 7

def solve(N, M, A):
    max = 0
    A.sort()

    for i in range(1, N):
        max += A[i] * cmb(i,  M-1, MOD)

    min = 0
    A.sort(reverse=True)
    for i in range(1, N):
        min += A[i] * cmb(i,  M-1, MOD)

    return int((max - min) % MOD)

A = list(map(int, input().split()))
def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 10 ** 9 + 7
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

print(solve(N, M, A))
