import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
visited = [0] * 100001

queue = deque([N])
visited[N] = 1

while queue:
    x = queue.popleft()

    if x == K:
        print(visited[x]-1)
        break

    for nx in [x+1, x-1, 2*x]:
        if 0 <= nx <= 100000 and visited[nx] == 0:
            visited[nx] = visited[x] + 1
            queue.append(nx)