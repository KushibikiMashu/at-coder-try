# see https://www.planeta.tokyo/entry/5195/

# 高速に組み合わせの数を求める
MOD = 10 ** 9 + 7
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

# 10^7程度が上限
# 必要なだけforを回す。N+1をa+1に書き換える
for i in range(2, n+1):
    fact.append((fact[-1] * i) % MOD)
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
    factinv.append((factinv[-1] * inv[-1]) % MOD)

# nCr n個から重複を許さずr個の組み合わせを選ぶ
# n!を求めている必要があるので、nが大きい場合（n=10^9など）はTLEになる
# cmb = n! * (n-r)!^-1 * r!^-1
def cmb(n, r):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % MOD

# n = 10^5なら回せる
# factinv（(r!)^-1）だけ計算できていたら、nのfact（n!）がなくても組み合わせを求めることができる
# ncr = n! * (n-r)!^-1 * r!^-1
def ncr(n, r):
    ret = factinv[r]
    for i in range(n, n-r, -1):
        ret = ret * i % MOD
    return ret

# -----
# nCrで

MOD = 10 ** 9 + 7

def prepare(n, MOD):
    # n! の計算
    f = 1
    for m in range(1, n + 1):
        f *= m
        f %= MOD
    fn = f

    # n!^-1 の計算
    inv = pow(f, MOD - 2, MOD)
    # n!^-1 - 1!^-1 の計算
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv

    return fn, invs


def ncr(n, r, invs, MOD):
    ret = invs[r]
    for i in range(n, n - r, -1):
        ret = ret * i % MOD
    return ret

# fnはr!, invsは(r!)^-1
fn, invs = prepare(r, MOD)
ncr(n, r, invs, MOD)

# -----
# combinationsの基本
# 3つから選ぶ

def cmb(n, r):
    if r < 0 or r > n:
        return 0
    if r == 1:
        return n
    elif r == 2:
        return n * (n-1) // 2
    else:
        return n * (n-1) * (n-2) // (3 * 2)

# -----
# 組み合わせを求める
from itertools import combinations
base = list(combinations("abcde",3))
