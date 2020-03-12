def solve():
    S = input()
    d = {}
    d['Sunny'] = 'Cloudy'
    d['Cloudy'] = 'Rainy'
    d['Rainy'] = 'Sunny'

    return d[S]

print(solve())
