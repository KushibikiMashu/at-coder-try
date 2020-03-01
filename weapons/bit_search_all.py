# bit全探索
# 組み合わせをlistにして返す
def int_to_list(bit, n):
    l = []
    for i in range(n):
     if bit & (1 << i):
         l.append(i)
    return l

N = 3
for i in range(1 << N):
    partial = int_to_list(i, N)

# print(partial)
# []
# [0]
# [1]
# [0, 1]
# [2]
# [0, 2]
# [1, 2]
# [0, 1, 2]
