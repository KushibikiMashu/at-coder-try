from collections import Counter

l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']
c = Counter(l)

print(c)
# 辞書型
# Counter({'a': 4, 'c': 2, 'b': 1})

print(c.items())
# dict_items([('a', 4), ('b', 1), ('c', 2)])

# 出現回数順に要素を取得
print(c.most_common())
# [('a', 4), ('c', 2), ('b', 1)]

print(c.most_common(2))
# [('a', 4), ('c', 2)]

# 文字列にも使える
s = 'supercalifragilisticexpialidocious'

print(s.count('p'))
# 2

c = Counter(s)

print(c)
# Counter({'i': 7, 's': 3, 'c': 3, 'a': 3, 'l': 3, 'u': 2, 'p': 2, 'e': 2, 'r': 2, 'o': 2, 'f': 1, 'g': 1, 't': 1, 'x': 1, 'd': 1})
