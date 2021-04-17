import sys


def dfs(n):
    if n == 81:
        for r in pan:
            print(*r)
        return True
    x = n // 9
    y = n % 9
    if pan[x][y] != 0:
        return dfs(n+1)
    else:
        for i in range(1,10):
            if not ck_row[x][i-1] and not ck_col[y][i-1] and not ck_squ[(x//3)*3+y//3][i-1]:
                ck_row[x][i-1] = ck_col[y][i-1] = ck_squ[(x//3)*3+y//3][i-1] = True
                pan[x][y] = i
                if dfs(n+1):
                    return True
                pan[x][y] = 0
                ck_row[x][i-1] = ck_col[y][i-1] = ck_squ[(x//3)*3+y//3][i-1] = False
    return False


ck_row = [[False]*9 for _ in range(9)]
ck_col = [[False]*9 for _ in range(9)]
ck_squ = [[False]*9 for _ in range(9)]

pan = []
for i in range(9):
    temp = list(map(int, sys.stdin.readline().split()))
    for j, c in enumerate(temp):
        if c != 0:
            ck_row[i][c-1] = True
            ck_col[j][c-1] = True
            ck_squ[(i//3)*3 + j//3][c-1] = True
    pan.append(temp)

dfs(0)

'''
def check(row, col, value):
    if pan[row][col] != 0:
        return False
    if ck_row[row][value-1]:
        return False
    if ck_col[col][value-1]:
        return False
    if ck_squ[(row//3)*3+col//3][value-1]:
        return False
    return True


def dfs(row):
    if row == 9:
        for r in pan:
            print(*r)
        return True
    for col in range(9):
        for val in range(1,10):
            if check(row, col, val):
                pan[row][col] = val
                ck_row[row][val-1] = ck_col[col][val-1] = ck_squ[(row//3)*3+col//3][val-1] = True
                if 0 in pan[row]:
                    flag = dfs(row)
                else:
                    flag = dfs(row+1)
                if flag:
                    return True
                else:
                    ck_row[row][val-1] = ck_col[col][val-1] = ck_squ[(row//3)*3+col//3][val-1] = False
                    pan[row][col] = 0
    return False
row단위에서 element단위로 바꿔서 함수 호출을 줄인다로 최적화
'''