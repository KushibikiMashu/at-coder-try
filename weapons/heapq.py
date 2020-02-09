# 優先度付きキュー

from heapq import heappush, heappop

# 最小値を取得する
q = []
heappush(q, 5)
heappush(q, 1)
heappush(q, 20)
# q = [1, 5, 20]
c = heappop(q)
# c = 1

# 最大値を取得する
q = []
heappush(q, -5)
heappush(q, -1)
heappush(q, -20)
# q = [-20, 5, -1]
c = -heappop(q)
# c = 20
