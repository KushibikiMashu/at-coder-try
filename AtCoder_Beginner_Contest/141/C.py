def solve():
    S = input()
    ans = 'Yes'
    for i, s in enumerate(S):
        if i% 2 == 0:
            if s == 'L':
                ans = 'No'
        else:
            if s == 'R':
                ans = 'No'

    return ans
