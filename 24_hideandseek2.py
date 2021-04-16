import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
visited = [[-1, 0] for _ in range(100001)]

queue = deque()
queue.append(N)
visited[N][0] = 0
visited[N][1] = 1

while queue:
    x = queue.popleft()

    for nx in [2*x, x+1, x-1]:
        if 0 <= nx <= 100000:
            if visited[nx][0] == -1:
                visited[nx][0] = visited[x][0] + 1
                visited[nx][1] = visited[x][1]
                queue.append(nx)
            elif visited[nx][0] == visited[x][0] + 1:
                visited[nx][1] += visited[x][1]

print(visited[K][0])
print(visited[K][1])