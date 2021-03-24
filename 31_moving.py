import sys

N, M = map(int, sys.stdin.readline().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(M):
        maxval = maze[i][j]
        if i != 0:
            maxval = max(maxval, maze[i][j] + maze[i-1][j])
        if j != 0:
            maxval = max(maxval, maze[i][j] + maze[i][j-1])
        if i != 0 and j != 0:
            maxval = max(maxval, maze[i][j] + maze[i-1][j-1])
        maze[i][j] = maxval

print(maze[N-1][M-1])


