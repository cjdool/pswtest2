
def findnear(number, lst):
    min = -1
    max = 10
    for j in range(1, 5):
        if not((number - j) in lst) and number-j >= 0:
            min = number - j
        if not((number + j) in lst) and number+j <= 9:
            max = number + j
        if min != -1 or max != 10:
            break
    return min, max

N = int(input())

nlist = [int(x) for x in str(N)]

M = int(input())

button = input()
butlist = button.split()
butlist = [int(i) for i in butlist]

bignum = 9
smlnum = 0

for i in range(10):
    if bignum in butlist:
        bignum -= 1
    else:
        break

for i in range(10):
    if smlnum in butlist:
        smlnum += 1
    else:
        break

bcnt = 0
flag = -1

for i in nlist:
    bcnt+=1
    if i in butlist and flag == -1:
        nmin, nmax = findnear(i, butlist)
        cmpval = i
        if nmin == -1: # max only
            flag = 1
        else:
            if nmax == 10: # min only
                flag = 0
            else: # min, max both
                flag = 2
    elif flag == 0:
        nmin = nmin*10+bignum
        cmpval = cmpval*10 + i
    elif flag == 1:
        nmax = nmax*10+smlnum
        cmpval = cmpval*10 + i
    elif flag == 2:
        nmin = nmin*10+bignum
        nmax = nmax*10+smlnum
        cmpval = cmpval*10 + i

if flag == 0:
    bcnt += cmpval - nmin
elif flag == 1:
    bcnt += nmax - cmpval
elif flag == 2:
    if cmpval - nmin > nmax - cmpval:
        bcnt += nmax - cmpval
    else:
        bcnt += cmpval - nmin

print(bcnt)


