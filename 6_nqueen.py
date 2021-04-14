import sys

N = int(sys.stdin.readline())


def basic_dfs(rootx, rooty):
    visit = [['x']*N for _ in range(N)]
    stack = [(rootx, rooty, visit, 0)]
    totalcnt = 0

    while stack:
        curx, cury, visited, cnt = stack.pop()
        if visited[curx][cury] == 'x':
            cnt += 1
            if cnt == N:
                totalcnt += 1
                continue
            pos = []
            for i in range(N):
                for j in range(N):
                    if visited[i][j] == 'o':
                        continue

                    if i == curx:
                        visited[i][j] = 'o'
                    elif j == cury:
                        visited[i][j] = 'o'
                    elif i+j == curx+cury:
                        visited[i][j] = 'o'
                    elif i-j == curx-cury:
                        visited[i][j] = 'o'
                    else:
                        pos.append((i, j))
            for x, y in pos:
                stack.append((x, y, visited, cnt))

    return totalcnt

nqueen = 0
for i in range(N):
    for j in range(N):
        nqueen += basic_dfs(i, j)
print(nqueen)






