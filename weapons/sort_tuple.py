from operator import itemgetter
A = [('b', 4), ('d', 2), ('c', 3), ('e', 1), ('a', 5)]
# タプルの2つ目の要素の昇順で並び替える
A.sort(key = itemgetter(1))
 # [('e', 1), ('d', 2), ('c', 3), ('b', 4), ('a', 5)]

# 左の次に右の要素でsort。降順
A.sort(key = itemgetter(0, 1), reverse=True)
# [('e', 1), ('d', 2), ('c', 3), ('b', 4), ('a', 5)]
