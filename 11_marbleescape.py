import sys
from collections import deque

curmap = []

def leftck(x):
    global curmap
    for i in range(x-1, (x//M)*M-1, -1):
        if curmap[i] == 'O':
            curmap[x] = '.'
            return False
        if curmap[i] == '#' or curmap[i] == 'B' or curmap[i] == 'R':
            curmap[x], curmap[i+1] = curmap[i+1], curmap[x]
            break
    return True


def rightck(x):
    global curmap
    for i in range(x+1, (x//M+1)*M):
        if curmap[i] == 'O':
            curmap[x] = '.'
            return False
        if curmap[i] == '#' or curmap[i] == 'B' or curmap[i] == 'R':
            curmap[x], curmap[i-1] = curmap[i-1], curmap[x]
            break
    return True


def topck(y):
    global curmap
    for j in range(y-M, -1, -M):
        if curmap[j] == 'O':
            curmap[y] = '.'
            return False
        if curmap[j] == '#' or curmap[j] == 'B' or curmap[j] == 'R':
            curmap[y], curmap[j+M] = curmap[j+M], curmap[y]
            break
    return True


def botck(y):
    global curmap
    for j in range(y+M, N*M, M):
        if curmap[j] == 'O':
            curmap[y] = '.'
            return False
        if curmap[j] == '#' or curmap[j] == 'B' or curmap[j] == 'R':
            curmap[y], curmap[j-M] = curmap[j-M], curmap[y]
            break
    return True


def bfs():
    queue = deque()
    queue.append(map)
    visitedstate = {map : 0}
    global curmap

    while queue:
        curstate = queue.popleft()
        cnt = visitedstate.get(curstate)

        if cnt > 9:
            return -1

        red = curstate.index('R')
        blue = curstate.index('B')
        cnt += 1

        # left shift
        curmap = list(curstate)
        if red < blue:
            if leftck(red):
                if leftck(blue):
                    nxtstate = ''.join(curmap)
                    if not visitedstate.get(nxtstate):
                        visitedstate[nxtstate] = cnt
                        queue.append(nxtstate)
            else:
                if leftck(blue):
                    return cnt
        else:
            if leftck(blue):
                if leftck(red):
                    nxtstate = ''.join(curmap)
                    if not visitedstate.get(nxtstate):
                        visitedstate[nxtstate] = cnt
                        queue.append(nxtstate)
                else:
                    return cnt

        # right shift
        curmap = list(curstate)
        if red > blue:
            if rightck(red):
                if rightck(blue):
                    nxtstate = ''.join(curmap)
                    if not visitedstate.get(nxtstate):
                        visitedstate[nxtstate] = cnt
                        queue.append(nxtstate)
            else:
                if rightck(blue):
                    return cnt
        else:
            if rightck(blue):
                if rightck(red):
                    nxtstate = ''.join(curmap)
                    if not visitedstate.get(nxtstate):
                        visitedstate[nxtstate] = cnt
                        queue.append(nxtstate)
                else:
                    return cnt

        # top shift
        curmap = list(curstate)
        if red < blue:
            if topck(red):
                if topck(blue):
                    nxtstate = ''.join(curmap)
                    if not visitedstate.get(nxtstate):
                        visitedstate[nxtstate] = cnt
                        queue.append(nxtstate)
            else:
                if topck(blue):
                    return cnt
        else:
            if topck(blue):
                if topck(red):
                    nxtstate = ''.join(curmap)
                    if not visitedstate.get(nxtstate):
                        visitedstate[nxtstate] = cnt
                        queue.append(nxtstate)
                else:
                    return cnt

        # bot shift
        curmap = list(curstate)
        if red > blue:
            if botck(red):
                if botck(blue):
                    nxtstate = ''.join(curmap)
                    if not visitedstate.get(nxtstate):
                        visitedstate[nxtstate] = cnt
                        queue.append(nxtstate)
            else:
                if botck(blue):
                    return cnt
        else:
            if botck(blue):
                if botck(red):
                    nxtstate = ''.join(curmap)
                    if not visitedstate.get(nxtstate):
                        visitedstate[nxtstate] = cnt
                        queue.append(nxtstate)
                else:
                    return cnt
    return -1


N, M = map(int, sys.stdin.readline().split())
map = ''
for _ in range(N):
    map += sys.stdin.readline().strip('\n')

print(bfs())