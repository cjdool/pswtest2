import sys

def ck(jari):
    sumx = 0
    for i in range(jari,-1,-1):
        sumx += result[i]
        if (sumx == 0 and h[i][jari-i] != '0') or (sumx < 0 and h[i][jari-i] != '-') or (sumx > 0 and h[i][jari-i] != '+'):
            return False
    return True

def dfs(jari):
    if jari == N:
        return True
    if h[jari][0] == '0':
        result[jari] = 0
        return dfs(jari+1)
    for i in range(1,11):
        if h[jari][0] == '+':
            result[jari] = i
        if h[jari][0] == '-':
            result[jari] = -i
        if ck(jari) and dfs(jari+1):
            return True
    return False

N = int(sys.stdin.readline())
S = sys.stdin.readline().strip('\n')

h = []
sidx = 0
for i in range(N):
    h.append(list(S[sidx:sidx+N-i]))
    sidx += N-i

result = [0] * N
dfs(0)
print(*result)

'''
def dfs(jari):
    if jari < 0:
        ans = []
        for i in range(N):
            ans.append(ck[i].index(1) - 10)
        print(*ans)
        exit(0)
    for i in range(21):
        ck[jari][i] = 1
        sumx = 0
        j = 0
        flag = True
        for case in h[jari]:
            sumx += ck[jari+j].index(1) - 10
            if (case == '+' and sumx <= 0) or (case == '-' and sumx >= 0) or (case == '0' and sumx != 0):
                flag = False
                break
            j += 1
        if flag:
            dfs(jari-1)
        ck[jari][i] = 0
    return

N = int(sys.stdin.readline())
S = sys.stdin.readline().strip('\n')

h = []
sidx = 0
for i in range(N):
    h.append(list(S[sidx:sidx+N-i]))
    sidx += N-i

ck = [[0] * 21 for _ in range(N)]
dfs(N-1)
'''
