import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

l = 0
r = N - 1
# ret = abs(arr[l] + arr[r])
ret = float('inf') # 최솟값 갖기 위하 큰 값으로 초기화
answer = [arr[l], arr[r]]

while(l < r): # 같은 경우는 안됨
    # 만약 answer보다 합(절댓값)이 작다면 갱신
    if abs(arr[l] + arr[r]) < ret:
        ret = abs(arr[l] + arr[r]) # ret 갱신
        answer = [arr[l], arr[r]] # 두 용액 갱신
        
    # sum 이 음수라면 left 증가, 양수라면 right 감소
    if arr[l] + arr[r] < 0:
        l += 1
    else:
        r -= 1

print(answer[0], answer[1])