A = list(input())

count = 0
while A:
    A = A[:-2]
    lenght = len(A) // 2
    if A[lenght:] == A[:lenght]:
        count = lenght * 2
        break

print(count)
