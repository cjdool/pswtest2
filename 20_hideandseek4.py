import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
visited = [0] * 100001
visitedlist = [0] * 100001

queue = deque()
queue.append(N)
visited[N] = 1

while queue:
    x = queue.popleft()

    if x == K:
        print(visited[x]-1)
        temp = [x]
        while x != N:
            x = visitedlist[x]
            temp.append(x)
        temp.reverse()
        print(*temp)
        break

    for nx in [2*x, x+1, x-1]:
        if 0 <= nx <= 100000 and visited[nx] == 0:
            visited[nx] = visited[x] + 1
            visitedlist[nx] = x
            queue.append(nx)