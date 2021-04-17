import sys

def bfs():
    queue = set()
    queue.add((0, 0, board[0][0]))
    result = 1
    while queue:
        x, y, lis = queue.pop()
        nxlist = [x-1, x+1, x, x]
        nylist = [y, y, y-1, y+1]
        for nx, ny in zip(nxlist, nylist):
            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in lis:
                queue.add((nx, ny, lis+board[nx][ny]))
                result = max(result, len(lis)+1)
    return result


R, C = map(int, sys.stdin.readline().split())
board = []
for _ in range(R):
    board.append(list(sys.stdin.readline().strip('\n')))


print(bfs())

'''
2 4
CADE
BTUW
3 3
ABC
AEF
YKG
'''