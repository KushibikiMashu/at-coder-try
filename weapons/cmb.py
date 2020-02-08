# see https://www.planeta.tokyo/entry/5195/

MOD = 10 ** 9 + 7
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % MOD)
    inv.append((-inv[p % i] * (p // i)) % MOD)
    factinv.append((factinv[-1] * inv[-1]) % MOD)

# nCr n個から重複を許さずr個の組み合わせを選ぶ
def cmb(n, r):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % MOD

# 組み合わせを求める
from itertools import combinations
base = list(combinations("abcde",3))
