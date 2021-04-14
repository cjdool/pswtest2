import sys

N = int(sys.stdin.readline())
pan = []
for _ in range(N):
    pan.append(list(map(int, sys.stdin.readline().split())))

case = [[0]*N for i in range(N)]
case[0][0] = 1

for i in range(N):
    for j in range(N):
        if pan[i][j] == 0:
            continue
        nx = j + pan[i][j]
        ny = i + pan[i][j]
        if nx < N:
            case[i][nx] += case[i][j]
        if ny < N:
            case[ny][j] += case[i][j]

print(case[N-1][N-1])