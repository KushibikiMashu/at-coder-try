def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    for a, b in enumerate(A):
        B.append((b, a+1))
    B.sort()
    l = []
    for (a, b) in B:
        l.append(b)
    print(*l)

# print(solve())

# def solve()が@return voidのとき
solve()

# テスト用
def resolve():
    solve()


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
2 3 1"""
        output = """3 1 2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """5
1 2 3 4 5"""
        output = """1 2 3 4 5"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """8
8 2 7 3 4 5 6 1"""
        output = """8 2 4 5 6 7 3 1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
