def solve():
    S = input()
    S = S.replace('eraser', '').replace('erase', '').replace('dreamer', '').replace('dream', '')
    return 'YES' if S == '' else 'NO'

print(solve())
