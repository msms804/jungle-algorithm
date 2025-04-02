# https://jyeonnyang2.tistory.com/279#google_vignette
# 어떤걸 이분탐색 해야?

import sys

N, C = map(int, sys.stdin.readline().split())
# print(N, C)
houses = []

for i in range(N):
    tmp = int(sys.stdin.readline())
    houses.append(tmp)


houses.sort()
# print(houses)

# 공유기 사이 거리를 기준으로 이분탐색해야
start = 1 # 집 사이 거리는 최소 1이므로
end = houses[-1] - houses[0]
answer = 0

while start <= end:
    cur = houses[0] # 현재
    cnt = 1 # 항상 1번째 집에 공유기 설치
    mid = (start + end) // 2

    for i in range(1, N):
        if houses[i] - cur >= mid:
            cnt += 1
            cur = houses[i]
    
    if cnt >= C:
        if answer < mid:
            answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)


