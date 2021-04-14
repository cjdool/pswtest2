import sys
from collections import deque
import copy

def checknextstate(vis, nxt):
    for vi in vis:
        if vi == nxt:
            return False
    return True


state = []

for i in range(3):
    state.append(list(map(int, sys.stdin.readline().split())))

answer = [[1,2,3],[4,5,6],[7,8,0]]
visitedstate = []
queue = deque()
queue.append((copy.deepcopy(state), 0))

flag = True
while queue:
    curstate, cnt = queue.popleft()
    visitedstate.append(copy.deepcopy(curstate))

    if curstate == answer:
        print(cnt)
        flag = False
        break

    bx = 0
    by = 0
    for i in range(3):
        for j in range(3):
            if curstate[i][j] == 0:
                bx = i
                by = j
                break

    nx = [bx-1, bx+1, bx, bx]
    ny = [by, by, by-1, by+1]
    for x, y in zip(nx, ny):
        if 0 <= x < 3 and 0 <= y < 3:
            nextstate = copy.deepcopy(curstate)
            nextstate[bx][by] = curstate[x][y]
            nextstate[x][y] = 0
            if checknextstate(visitedstate, nextstate):
                queue.append((nextstate, cnt+1))

if flag:
    print(-1)

'''
1 3 0
4 2 5
7 8 6
'''