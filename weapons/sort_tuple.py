from operator import itemgetter
A = [('b', 4), ('d', 2), ('c', 3), ('e', 1), ('a', 5)]
# 右側の要素でsort
A.sort(key = itemgetter(1))
 # [('e', 1), ('d', 2), ('c', 3), ('b', 4), ('a', 5)]

# 左の次に右の要素でsort。降順
from operator import itemgetter
A.sort(key = itemgetter(0, 1), reverse=True)
# [('e', 1), ('d', 2), ('c', 3), ('b', 4), ('a', 5)]
