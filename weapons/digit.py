# 10進数Xをn進数に変換する
def ten_to_n(X, n):
    i = X // n
    s = str(X % n)
    if (i):
        return ten_to_n(i, n) + s
    return s

# X = 11, n = 2
# i sを出力する
# 5 1
# 2 1
# 1 0
# 0 1
# 4
