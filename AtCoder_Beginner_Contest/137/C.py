from collections import defaultdict

def solve():
    N = int(input())
    d = defaultdict(int)
    c = 0
    for _ in range(N):
        a = ''.join(sorted(list(input())))
        if a in d:
            c += d[a]
            d[a] += 1
        else:
            d[a] = 1
    return c

# print(solve())

# def solve()が@return voidのとき
# solve()

# テスト用
def resolve():
    print(solve())
#     solve()


import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """3
acornistnt
peanutbomb
constraint"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """2
oneplustwo
ninemodsix"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """5
abaaaaaaaa
oneplustwo
aaaaaaaaba
twoplusone
aaaabaaaaa"""
        output = """4"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
