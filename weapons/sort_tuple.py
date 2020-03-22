from operator import itemgetter
A = [('b', 4), ('d', 2), ('c', 3), ('e', 1), ('a', 5)]
# 右側の要素でsort
A.sort(key = itemgetter(1))
 # [('e', 1), ('d', 2), ('c', 3), ('b', 4), ('a', 5)]

# 左の次に右の要素でsort。降順
from operator import itemgetter
A.sort(key = itemgetter(0, 1), reverse=True)
# [('e', 1), ('d', 2), ('c', 3), ('b', 4), ('a', 5)]


# 複数のキーで昇順、降順をバラバラにソートする
# 例: タプルのキー0は昇順で、キー1で降順でソートする
from operator import itemgetter
def multisort(l, specs):
    for key, reverse in reversed(specs):
        l.sort(key=itemgetter(key), reverse=reverse)
    return l

l = multisort(l, [(0, False), (1, True)])

# 上記は、下記と同値
l = []
l.sort(key=itemgetter(1), reverse=True)
l.sort(key=itemgetter(0), reverse=False)
# （この順番じゃないとだめ。直感と逆の順番になることに注意）
