import sys
from itertools import permutations


N = int(sys.stdin.readline())
S = sys.stdin.readline().strip('\n')
su = list(range(-10, 11))
caselist = permutations(su, N)

for case in caselist:
    caseanswer = ''
    for i in range(N):
        sumx = 0
        for j in range(i, N):
            sumx += case[j]
            if sumx > 0:
                caseanswer = caseanswer + '+'
            elif sumx == 0:
                caseanswer = caseanswer + '0'
            else:
                caseanswer = caseanswer + '-'
    if caseanswer == S:
        case = list(case)
        print(*case)
        break
