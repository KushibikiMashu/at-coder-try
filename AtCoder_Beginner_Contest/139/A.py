def solve():
    N = int(input())
    A = list(map(int, input().split()))
    tmp = 0
    ans = 0
    for i in range(N-1):
        if A[i] < A[i+1]:
            tmp = 0
        else:
            tmp += 1
        ans = max(ans, tmp)

    return ans

print(solve())
