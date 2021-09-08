import sys

N, M = map(int, sys.stdin.readline())
paper = []
for _ in range(M):
    paper.append(list(map(int, sys.stdin.readline().strip('\n'))))