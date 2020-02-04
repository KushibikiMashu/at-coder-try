a = [i for i in range(11)]
s = [0]
for i in a:
    s.append(s[-1] + i)
print(s[3] - s[0]) # 0 + 1 + 2 = 3
print(s[11] - s[8]) # 8 + 9 + 10 = 27
