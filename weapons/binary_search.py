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
