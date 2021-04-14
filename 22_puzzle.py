import sys
from collections import deque

state = ''
for i in range(3):
    state += ''.join(sys.stdin.readline().split())

queue = deque()
queue.append(state)
visited = {state : 0}

flag = True
while queue:
    curstate = queue.popleft()
    cnt = visited.get(curstate)
    x = curstate.index('0')

    if curstate == '123456780':
        print(cnt)
        flag = False
        break

    cnt += 1
    i = x // 3
    j = x % 3

    curstatelist = list(curstate)
    if i > 0:
        curstatelist[x], curstatelist[x-3] = curstatelist[x-3], curstatelist[x]
        nxtstatedict = ''.join(curstatelist)
        if not visited.get(nxtstatedict):
            visited[nxtstatedict] = cnt
            queue.append(nxtstatedict)
        curstatelist[x], curstatelist[x-3] = curstatelist[x-3], curstatelist[x]
    if i < 2:
        curstatelist[x], curstatelist[x+3] = curstatelist[x+3], curstatelist[x]
        nxtstatedict = ''.join(curstatelist)
        if not visited.get(nxtstatedict):
            visited[nxtstatedict] = cnt
            queue.append(nxtstatedict)
        curstatelist[x], curstatelist[x+3] = curstatelist[x+3], curstatelist[x]
    if j > 0:
        curstatelist[x], curstatelist[x-1] = curstatelist[x-1], curstatelist[x]
        nxtstatedict = ''.join(curstatelist)
        if not visited.get(nxtstatedict):
            visited[nxtstatedict] = cnt
            queue.append(nxtstatedict)
        curstatelist[x], curstatelist[x-1] = curstatelist[x-1], curstatelist[x]
    if j < 2:
        curstatelist[x], curstatelist[x+1] = curstatelist[x+1], curstatelist[x]
        nxtstatedict = ''.join(curstatelist)
        if not visited.get(nxtstatedict):
            visited[nxtstatedict] = cnt
            queue.append(nxtstatedict)
        curstatelist[x], curstatelist[x+1] = curstatelist[x+1], curstatelist[x]

if flag:
    print(-1)

'''
1 3 0
4 2 5
7 8 6
'''