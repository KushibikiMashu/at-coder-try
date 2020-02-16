def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    ans = 0
    for i in range(0, N-1, 2):
        ans += A[i] - A[i+1]
    if N % 2 == 1:
        ans += A[-1]
    return ans

print(solve())
