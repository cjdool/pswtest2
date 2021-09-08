import sys
from collections import deque

def bfs():
    queue = deque()
    if '.' in bp[0]:
        idx = bp[0].index('.')
        queue.append((0, idx, 0, 0))
        visited[0][idx] = 1
    if '#' in bp[0]:
        idx = bp[0].index('#')
        queue.append((0, idx, 1, 0))
        visited[0][idx] = 1
    if '$' in bp[0]:
        idx = bp[0].index('$')
        queue.append((0, idx, 1, 1))
        visited[0][idx] = 1

    if '.' in bp[-1]:
        idx = bp[-1].index('.')
        queue.append((h-1, idx, 0, 0))
        visited[-1][idx] = 1
    if '#' in bp[-1]:
        idx = bp[-1].index('#')
        queue.append((h-1, idx, 1, 0))
        visited[-1][idx] = 1
    if '$' in bp[0]:
        idx = bp[-1].index('$')
        queue.append((h-1, idx, 1, 1))
        visited[-1][idx] = 1




    while queue:
        x, y, dcnt, pcnt = queue.popleft()
        if pcnt == 2:
            return dcnt



N = int(sys.stdin.readline())
for _ in range(N):
    h, w = map(int, sys.stdin.readline().split())
    bp = []
    visited = [[0]*w for _ in range(h)]
    for i in range(h):
        bp.append(sys.stdin.readline().strip('\n'))
    print(bfs())
