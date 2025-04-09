import sys

n = int(sys.stdin.readline())
d = [0] * 91

def Fibo(x):
    if x == 0: return 0
    if x == 1: return 1

    if d[x] != 0: return d[x]

    d[x] = Fibo(x - 1) + Fibo(x - 2)

    return d[x]

print(Fibo(n))
