import sys

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return int(a*b/gcd(a, b))

T = int(sys.stdin.readline())

for _ in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())

    les = lcm(M, N)

    if M > N:
        q = M
        r = x
        q2 = N
        r2 = y
    elif M == N:
        q = M
        q2 = N
        if x > y:
            r = x
            r2 = y
        else:
            r = y
            r2 = x
    else:
        q = N
        r = y
        q2 = M
        r2 = x
    if q2 == r2:
        r2 = 0

    temp = r
    flag = True
    while temp <= les:
        if (q2 == 1 and r2 == temp) or (r2 == temp % q2):
            flag = False
            print(temp)
            break
        temp += q

    if flag:
        print(-1)

'''
1 1 1
2 2 2
...
10 10 10
11 1 11
12 2 12
13 3 1

? 3 9 --> 10a+3 and 12b+9
'''