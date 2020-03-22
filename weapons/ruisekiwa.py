from itertools import accumulate

ary = [1, 3, 5, 7, 9]
cumsum = accumulate(ary)
print(list(cumsum))
# -> [1, 4, 9, 16, 25]
