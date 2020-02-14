# 数字の各桁の和
n = 12345
result = sum(list(map(int, str(n))))
print(result) # 15

# 下一桁
n = 12345
last_digit = str(n)[-1]
print(last_digit) # 5

# 辞書の扱い
