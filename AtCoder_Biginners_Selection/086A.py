import sys
from io import StringIO
import unittest

def solve():
    N, M = map(int, input().split())
    return 'Even' if N % 2 == 0 or M % 2 == 0 else 'Odd'

print(solve())

# テスト用
def resolve():
    print(solve())

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
        input = """3 4"""
        output = """Even"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """1 21"""
        output = """Odd"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
