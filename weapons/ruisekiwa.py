import itertools

ary = [1, 3, 5, 7, 9]
cumsum = itertools.accumulate(ary)
print(list(cumsum))
# -> [1, 4, 9, 16, 25]
