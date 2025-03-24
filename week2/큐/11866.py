from collections import deque

N, K = map(int, input().split())

nums = deque(list(range(1, N + 1)))

print("<", end="")
cnt = 1
result = []
while nums:
    tmp = nums.popleft()
    
    if cnt == K:
        result.append(tmp)
        cnt = 0
    else:   
        nums.append(tmp)
    cnt += 1

print(", ".join(map(str, result)), end=">")