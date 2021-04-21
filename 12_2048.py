import sys
from copy import deepcopy

def move(dir):
    if dir == 0: # left
        for i in range(N):
            k = 0
            for j in range(1,N):
                if pan[i][j]:
                    temp = pan[i][j]
                    pan[i][j] = 0
                    if pan[i][k] == 0:
                        pan[i][k] = temp
                    elif pan[i][k] == temp:
                        pan[i][k] = 2 * temp
                        k += 1
                    else:
                        k += 1
                        pan[i][k] = temp
    elif dir == 1: # right
        for i in range(N):
            k = N-1
            for j in range(N-2, -1, -1):
                if pan[i][j]:
                    temp = pan[i][j]
                    pan[i][j] = 0
                    if pan[i][k] == 0:
                        pan[i][k] = temp
                    elif pan[i][k] == temp:
                        pan[i][k] = 2 * temp
                        k -= 1
                    else:
                        k -= 1
                        pan[i][k] = temp
    elif dir == 2: # top
        for j in range(N):
            k = 0
            for i in range(1, N):
                if pan[i][j]:
                    temp = pan[i][j]
                    pan[i][j] = 0
                    if pan[k][j] == 0:
                        pan[k][j] = temp
                    elif pan[k][j] == temp:
                        pan[k][j] = 2 * temp
                        k += 1
                    else:
                        k += 1
                        pan[k][j] = temp
    else:
        for j in range(N):
            k = N-1
            for i in range(N-2, -1, -1):
                if pan[i][j]:
                    temp = pan[i][j]
                    pan[i][j] = 0
                    if pan[k][j] == 0:
                        pan[k][j] = temp
                    if pan[k][j] == temp:
                        pan[k][j] = 2 * temp
                        k -= 1
                    else:
                        k -= 1
                        pan[k][j] = temp



def dfs(cnt):
    global maxval, pan

    if cnt == 5:
        maxval = max(maxval, max(map(max, pan)))
        return

    temppan = deepcopy(pan)
    for i in range(4):
        move(i)
        dfs(cnt+1)
        pan = deepcopy(temppan)


N = int(sys.stdin.readline())

pan = []
for _ in range(N):
    pan.append(list(map(int, sys.stdin.readline().split())))

maxval = 0
dfs(0)
print(maxval)

