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

# factorize(900)
# [2, 2, 3, 3, 5, 5]

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

# factorize(900)
# [(2, 2), (3, 2), (5, 2)]

n = int(input())
ans = 0
while n > 0:
    ans = len(factorize(n))
    n -= 1
print(ans)
