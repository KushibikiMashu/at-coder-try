def solve():
    N, M = map(int, input().split())
    l = [i for i in range(M-(N-1), M+(N-1)+1)]
    print(*l)

# solve()

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
        input = """3 7"""
        output = """5 6 7 8 9"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """4 0"""
        output = """-3 -2 -1 0 1 2 3"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """1 100"""
        output = """100"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
