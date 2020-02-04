A = list(input())
n = len(A)
l = [0] * (n+1)
count = 0

for i in range(n):
    if A[i] == '<':
        count += 1
        l[i+1] = count
    else:
        count = 0

A.reverse()
l.reverse()
count = 0

for i in range(n):
    if A[i] == '>':
        count += 1
        l[i+1] = max(count, l[i+1])
    else:
        count = 0

print(sum(l))
