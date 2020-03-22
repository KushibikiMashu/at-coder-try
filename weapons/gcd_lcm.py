# 最大公約数
# 例: x=8, y=12のとき、最大公約数は4
from fractions import gcd
gcd(x, y)

# 最小公倍数
# 最小公倍数は、数x, yを掛けたものを、最大公約数で割ったもの
# 例: x=10, y=12の時、gcdは2なので、最小公倍数は10 * 12 / 2 = 60
from fractions import gcd
def lcm(x, y):
    return (x * y) // gcd(x, y)

from functools import reduce
def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)

def lcm_list(numbers):
    return reduce(lcm, numbers)
