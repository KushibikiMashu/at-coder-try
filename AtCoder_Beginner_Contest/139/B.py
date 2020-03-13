import math
def solve():
    N, M = map(int, input().split())
    return math.ceil((M-1)/(N-1))

print(solve())
