# タプルの2つ目の要素の昇順で並び替える

from operator import itemgetter
A = [('b', 4), ('d', 2), ('c', 3), ('e', 1), ('a', 5)]
A.sort(key = itemgetter(1)) # [('e', 1), ('d', 2), ('c', 3), ('b', 4), ('a', 5)]
