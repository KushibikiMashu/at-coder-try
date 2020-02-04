n = int(input())
aaa = list(map(int, input().split()))

MOD = 10 ** 9 + 7
ans = 0
m = 1
for i in range(60):
    one_count = sum(a & m for a in aaa)
    # 全ての数のi桁目の1の個数
    one_count //= m
    # 全ての数のi桁目の0の個数
    zero_count = n - one_count
    # XORは、one_count * zero_count * 2 ** iで算出できる
    ans = (ans + one_count * zero_count * m) % MOD
    m *= 2

print(ans)
