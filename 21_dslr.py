import sys
from collections import deque

N = int(sys.stdin.readline())
for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())
    visited = [0] * 10000
    queue = deque()
    queue.append((A, ''))
    visited[A] = 1

    while queue:
        x, cmd = queue.popleft()

        if x == B:
            print(cmd)
            break

        nx = (x * 2) % 10000
        if visited[nx] == 0:
            visited[nx] = 1
            queue.append((nx, cmd+'D'))
        nx = x-1 if x != 0 else 9999
        if visited[nx] == 0:
            visited[nx] = 1
            queue.append((nx, cmd+'S'))
        nx = int(x % 1000 * 10 + x / 1000)
        if visited[nx] == 0:
            visited[nx] = 1
            queue.append((nx, cmd+'L'))
        nx = int(x % 10 * 1000 + x / 10)
        if visited[nx] == 0:
            visited[nx] = 1
            queue.append((nx, cmd+'R'))