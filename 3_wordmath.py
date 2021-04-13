import sys

N = int(sys.stdin.readline())
inlist = []
cnt = {}
for _ in range(N):
    temp = sys.stdin.readline().strip()
    inlist.append(temp)
    length = len(temp)
    for i in range(length):
        if temp[i] in cnt:
            cnt[temp[i]] += 1 * (10 ** (length-1-i))
        else:
            cnt[temp[i]] = 1 * (10 ** (length-1-i))

scnt = sorted(cnt.items(), reverse=True, key=lambda item:item[1])
cnt = {}
i = 9
for key, val in scnt:
    cnt[key] = i
    i -= 1

sum = 0
for item in inlist:
    curnum = ''
    for c in item:
        curnum += str(cnt[c])
    sum += int(curnum)

print(sum)

'''
5
ACDEB
KGCF
ADEB
CFEK
KBAA
'''