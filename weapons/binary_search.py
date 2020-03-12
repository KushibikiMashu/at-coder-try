list = [1,2,3,4,5]
x = 2

def binary_search(list, x):
    l = 0
    r = len(list)
    while l-r <= -1:
        mid = (l + r) // 2
        if list[mid] == x:
            return mid
        elif list[mid] < x:
            l = mid
        else:
            r = mid

# listのindexである1が出力される
print(binary_search(list, x))

# 0から10++9+1の間で、条件A * mid + B * len(str(mid))を満たす最大の整数を探す
def binary_search():
    A, B, X = map(int, input().split())
    l = 0
    r = 10 ** 9 + 1
    while r-l > 1:
        mid = (l + r) // 2
        if A * mid + B * len(str(mid)) <= X:
            l = mid
        else:
            r = mid

    return l

