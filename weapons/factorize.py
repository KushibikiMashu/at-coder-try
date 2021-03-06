# 素因数を列挙する
def factorize(n):
    b = 2
    fct = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        b = b + 1
    if n > 1:
        fct.append(n)
    return fct

factorize(900) # [2, 2, 3, 3, 5, 5]

def factorize(n):
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct

factorize(900) # [(2, 2), (3, 2), (5, 2)]

# 約数の個数を数える
def count_divisor(n):
    count = 1
    divisor = 2
    while divisor * divisor <= n:
        degree = 0 # 次数
        while n % divisor == 0:
            n = n // divisor
            degree += 1
        divisor += 1
        count *= (degree + 1)
    if n > 1:
        count *= 2
    return count

# 1, 2, 3, 4, 5, 6, ... 300, 450, 900
print(count_divisor(900)) # 27
