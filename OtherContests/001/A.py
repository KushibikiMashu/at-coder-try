H, W = map(int, input().split())
field = []

for i in range(H):
    line= input()
    field.append(line)

for i in range(H):
    for j in range(W):
        if field[i][j] == 's':
            sh = i
            sw = j
        if field[i][j] == 'g':
            gh = i
            gw = j
