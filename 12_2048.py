import sys
from collections import deque

def bfs():
    queue = deque()
    queue.append((0, pan))
    maxval = 2

    while queue:
        cnt, curstate = queue.popleft()

        if cnt == 5:
            maxval = max(maxval, max(map(max, curstate)))
            continue

        cnt += 1
        # left shift
        nxtstate = [[0]*N for _ in range(N)]
        for i in range(N):
            j = 0
            k = 0
            while j < N-1:
                if curstate[i][j] != 0:
                    if curstate[i][j] == curstate[i][j+1]:
                        nxtstate[i][k] = 2*curstate[i][j]
                        j += 1
                    else:
                        nxtstate[i][k] = curstate[i][j]
                    k += 1
                j += 1
            if j == N-1:
                nxtstate[i][k] = curstate[i][j]
        queue.append((cnt, nxtstate))
        # right shift
        nxtstate = [[0]*N for _ in range(N)]
        for i in range(N):
            j = N-1
            k = N-1
            while j > 0:
                if curstate[i][j] != 0:
                    if curstate[i][j] == curstate[i][j-1]:
                        nxtstate[i][k] = 2*curstate[i][j]
                        j -= 1
                    else:
                        nxtstate[i][k] = curstate[i][j]
                    k -= 1
                j -= 1
            if j == 0:
                nxtstate[i][k] = curstate[i][j]
        queue.append((cnt, nxtstate))
        # top shift
        nxtstate = [[0]*N for _ in range(N)]
        for j in range(N):
            i = 0
            k = 0
            while i < N-1:
                if curstate[i][j] != 0:
                    if curstate[i][j] == curstate[i+1][j]:
                        nxtstate[k][j] = 2*curstate[i][j]
                        i += 1
                    else:
                        nxtstate[k][j] = curstate[i][j]
                    k += 1
                i += 1
            if i == N-1:
                nxtstate[k][j] = curstate[i][j]
        queue.append((cnt, nxtstate))
        # bot shift
        nxtstate = [[0]*N for _ in range(N)]
        for j in range(N):
            i = N-1
            k = N-1
            while i > 0:
                if curstate[i][j] != 0:
                    if curstate[i][j] == curstate[i-1][j]:
                        nxtstate[k][j] = 2*curstate[i][j]
                        i -= 1
                    else:
                        nxtstate[k][j] = curstate[i][j]
                    k -= 1
                i -= 1
            if i == 0:
                nxtstate[k][j] = curstate[i][j]
        queue.append((cnt, nxtstate))

    return maxval


N = int(sys.stdin.readline())

pan = []
for _ in range(N):
    pan.append(list(map(int, sys.stdin.readline().split())))

print(bfs())