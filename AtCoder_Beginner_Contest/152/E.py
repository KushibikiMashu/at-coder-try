import fractions

N = int(input())
A = list(map(int, input().split()))

def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

def solve():
    memo = A[0]
    for i in range(N - 1):
        memo = lcm(memo, A[i + 1])

    ans = 0
    for i in range(N):
        ans += memo // A[i]

    return ans % (10 ** 9 + 7)

print(solve())
