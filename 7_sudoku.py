import sys


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
                ck_row[row][val-1] = True
                ck_col[col][val-1] = True
                ck_squ[(row//3)*3+col//3][val-1] = True
                if 0 in pan[row]:
                    flag = dfs(row)
                else:
                    flag = dfs(row+1)
                if flag:
                    return True
                else:
                    pan[row][col] = 0
                    ck_row[row][val-1] = False
                    ck_col[col][val-1] = False
                    ck_squ[(row//3)*3+col//3][val-1] = False
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
