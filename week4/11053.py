import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
# i 번째 원소까지 고려했을때 가장 긴 증가하는 부분수열의 개수
dp = [1] * (N + 1) 

for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            # i 보다 앞쪽에 있는 숫자들과 비교하면서 최댓값 유지함
            dp[i] = max(dp[i] , dp[j] + 1)
print(max(dp))