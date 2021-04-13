import sys
from itertools import combinations

N = int(sys.stdin.readline())
inlist = []
people = []
for i in range(N):
    inlist.append(list(map(int, sys.stdin.readline().split())))
    people.append(i)

ncr = list(combinations(people, int(N/2)))
scores = []
for case in ncr:
    caselist = list(case)
    casesum = 0
    for i in combinations(caselist, 2):
        casesum += inlist[i[0]][i[1]] + inlist[i[1]][i[0]]
    scores.append(casesum)

ncrp1 = scores[0:int(len(ncr)/2)]
ncrp2 = scores[int(len(ncr)/2):]
ncrp2.reverse()
difflist = []
for p1, p2 in zip(ncrp1, ncrp2):
    difflist.append(abs(p1-p2))
print(min(difflist))
