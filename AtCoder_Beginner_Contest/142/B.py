def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    l = list(filter(lambda x: x >= M, A))
    return len(l)

print(solve())

# def solve()が@return voidのとき
# solve()

# テスト用
def resolve():
    print(solve())


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
        input = """4 150
150 140 100 200"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """1 500
499"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """5 1
100 200 300 400 500"""
        output = """5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
