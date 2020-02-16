def solve():
    N = int(input())
    A = [[0,0,0]]
    for _ in range(N):
        a = list(map(int, input().split()))
        A.append(a)

    ans = 'Yes'

    for i in range(N):
        t1, x1, y1 = A[i]
        t2, x2, y2 = A[i+1]

        time = t2 - t1
        x = abs(x2 - x1)
        y = abs(y2 - y1)

        if time < x+y or (time+x+y) % 2 != 0:
            ans = 'No'
            exit()

    return ans

print(solve())
