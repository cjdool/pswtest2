import sys
import copy

N = int(sys.stdin.readline())


def basic_dfs(rootx, rooty):
    answerlist = []
    stack = [(rootx, rooty, [['x']*N for _ in range(N)], 0)]
    totalcnt = 0

    while stack:
        curx, cury, visited2, cnt = stack.pop()
        visited = copy.deepcopy(visited2)
        pos = []
        for i in range(N):
            for j in range(N):
                if visited[i][j] == 'o' or visited[i][j] == 'q':
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
                    if rootx < i or (rootx == i and rooty < j):
                        pos.append((i, j))
        visited[curx][cury] = 'q'
        cnt += 1
        if cnt == N:
            flag = True
            for ans in answerlist:
                if ans == visited:
                    flag = False
                    break
            if flag:
                totalcnt += 1
                answerlist.append(visited)
            continue
        for x, y in pos:
            stack.append((x, y, visited, cnt))

    return totalcnt

nqueen = 0
for i in range(N):
    for j in range(N):
        nqueen += basic_dfs(i, j)
print(nqueen)






