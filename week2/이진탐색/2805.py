import sys

N, M = map(int, sys.stdin.readline().split())

trees = list(map(int, sys.stdin.readline().split()))

low = 0
high = max(trees)

res = 0
answer = 0

ret = sum(trees) # 여기다 최소 차이 나는거 갱신 해야할듯
while low <= high:
    mid = (low + high) // 2
    for t in trees:
        if t > mid:
            res += t - mid
            
    # print("중간값", mid, end=" ")

    if res >= M:
        answer = mid
        # print("중간값보다 큼", end=" ")
        low = mid + 1
    else: 
        # print("중간값보다 작음", end=" ")
        high = mid - 1

    # print("가져갈 수 있는 나무: ", res)
    
    res = 0
    # if abs(res - M) < ret: # 가져갈 수 있는 나무, 중간값 차의 절댓값
    #     ret = abs(res - M)
    #     answer = mid 

    # res = 0
    
print(answer)