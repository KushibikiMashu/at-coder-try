import itertools

bi = [0,0,0,1,1,0,0,0,1,1,0,1]

gr = itertools.groupby(bi)
for key, group in gr:
    print(f'{key}: {list(group)}')

# 0: [0, 0, 0]
# 1: [1, 1]
# 0: [0, 0, 0]
# 1: [1, 1]
# 0: [0]
# 1: [1]

# ソートするといい

# import itertools
# gr = itertools.groupby(bi)
# for key, group in gr:
#     a
