import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
breaklist = list(sys.stdin.readline().split())
minval = abs(N-100)


def check(number):
    number = list(str(number))
    for digit in number:
        if digit in breaklist:
            return False
    return True


for i in range(1000001):
    if check(i):
        minval = min(minval, len(str(i)) + abs(i-N))

print(minval)


'''
from itertools import product
normallist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
flag = True
minval = abs(N-100)
digitnum = len(str(N))
for item in breaklist:
    if item == 0:
        flag = False
    normallist.remove(item)

if flag:
    lst = product(normallist, repeat=digitnum+1)

    for item in lst:
        x = int(''.join(map(str, item)))
        dig = len(str(x))
        minval = min(minval, dig+abs(x - N))

    print(minval)
else:
    for i in range(3):
        if digitnum-1+i == 0:
            continue
        lst = product(normallist, repeat=digitnum-1+i)
        for item in lst:
            x = int(''.join(map(str, item)))
            dig = len(str(x))
            minval = min(minval, dig+abs(x - N))

    print(minval)
'''