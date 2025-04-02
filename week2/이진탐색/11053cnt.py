import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
cnt = [0] * N
ret = 0
# 10 20 10 30 20 50

for i in range(N):
    maxValue = 0
    for j in range(i):
        if arr[j] < arr[i] and maxValue < cnt[j]: # maxValue < cnt[j]는 10 30의 경우
            maxValue = cnt[j]
    cnt[i] = maxValue + 1
    ret = max(ret, cnt[i])
# print(cnt)
print(ret)