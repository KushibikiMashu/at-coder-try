# 全ての要素に対して、何回2で割れるか計算する
def solve():
    N = int(input())
    A = list(map(int, input().split()))
    l = []

    for a in A:
        if a % 2 == 0:
            c = 0
            while a % 2 == 0:
                a //= 2
                c += 1
            l.append(c)
        else:
            l.append(0)

    return min(l)

print(solve())

# 全ての要素を順番に2でわっていき、初めて奇数が現れるまで割れた回数を回答とする
def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    while True:
        for i in range(N):
            if A[i] % 2 != 0:
                return ans // N
            A[i] //= 2
            ans += 1

    return ans

print(solve())
