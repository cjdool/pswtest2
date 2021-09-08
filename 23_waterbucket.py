import sys
from collections import deque

A, B, C = map(int,sys.stdin.readline().split())

pan = 0
b = 0
c = C
state = [pan, b, c]

queue = deque()
queue.append(state)
visitedstate = [state]

while queue:
    curstate = queue.popleft()
    pan = curstate[0]
    b = curstate[1]
    c = curstate[2]

    case = [(pan, b, B), (pan, c, C), (b, pan, A), (b, c, C), (c, pan, A), (c, b, B)]

    i = 1
    for x, y, z in case:
        if x != 0:
            if x+y > z:
                x, y = x+y-z, z
            else:
                x, y = 0, x+y
            if i == 1:
                nxtstate = [x,y,c]
            elif i == 2:
                nxtstate = [x,b,y]
            elif i == 3:
                nxtstate = [y,x,c]
            elif i == 4:
                nxtstate = [pan, x, y]
            elif i == 5:
                nxtstate = [y,b,x]
            else:
                nxtstate = [pan, y, x]
            if nxtstate not in visitedstate:
                visitedstate.append(nxtstate)
                queue.append(nxtstate)
        i += 1

ans = set()
for vstate in visitedstate:
    if vstate[0] == 0:
        ans.add(vstate[2])
print(*sorted(list(ans)))
