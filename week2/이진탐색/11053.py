import sys
# 이걸 이분탐색으로 어케풀지
# 그냥 for문 돌리면 안되나?
# 6
# 10 20 10 30 20 50

# N = int(sys.stdin.readline())
# arr = list(map(int, sys.stdin.readline().split()))
# max_a = arr[0]
# res = [max_a]
# 1. 최댓값을 첫번째 요소로
# 2. 최댓값보다 큰 요소 만나면 최댓값 갱신?
# 3. 최댓값보다 큰것만 res에 append
# 이렇게 하면 안됨, 반례가 1 3 5 2 4 6 7

# for a in arr:
#     if a > max_a:
#         res.append(a)
#         max_a = a

# print(len(res))

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
ret = []

for a in arr:
    if len(ret) == 0:
        ret.append(a)
        continue

    if ret[-1] < a : # 증가하면 추가
        ret.append(a)
    else: # 이분탐색으로 위치 바꿔야 한다고..
        ret