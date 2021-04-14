import sys
import copy

N = int(sys.stdin.readline())

answerlist = []

def basic_dfs(rootx, rooty):
    stack = [[(rootx, rooty)]]

    while stack:
        qlist = stack.pop()

        if len(qlist) == N:
            flag = True
            qlist.sort(key=lambda tup: tup[0])
            for ans in answerlist:
                if ans == qlist:
                    flag = False
                    break
            if flag:
                answerlist.append(qlist)
            continue

        pos = []
        for i in range(N):
            for j in range(N):
                flag = True
                for queenx, queeny in qlist:
                    if flag:
                        # 가로
                        if queenx == i:
                            flag = False
                            break
                        # 세로
                        if queeny == j:
                            flag = False
                            break
                        # 대각1
                        if queenx + queeny == i + j:
                            flag = False
                            break
                        # 대각2
                        if queenx - queeny == i - j:
                            flag = False
                            break
                if flag:
                    pos.append((i, j))

        for x, y in pos:
            qlist2 = copy.deepcopy(qlist)
            qlist2.append((x, y))
            stack.append(qlist2)
    return


for i in range(N):
    for j in range(N):
        basic_dfs(i, j)
print(len(answerlist))






