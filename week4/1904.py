import sys

N = int(sys.stdin.readline())
d = [0] * 1000001

# 탑다운
# def F(x):
#     if x == 1: return 1
#     if x == 2: return 2
#     if d[x] != 0: return d[x]

#     # 파이썬의 재귀 깊이가 1000이라 이것못함(100만)
#     d[x] = (F(x - 1) + F(x - 2)) % 15746

#     return d[x]

# print(F(N))

# 바텀업
def T(x):
    d[1] = 1
    d[2] = 2

    for i in range(3, x + 1):
        d[i] = (d[i - 1] + d[i - 2]) % 15746

T(N)
print(d[N])