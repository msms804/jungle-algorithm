import sys
from collections import deque

N = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split())) # 이걸 큐로 해야하나

op = list(map(int, sys.stdin.readline().split()))
# print(nums, op)
max_result = -1_000_000_000  # 문제에서 보장된 최소값
min_result = 1_000_000_000   # 문제에서 보장된 최대값

def go(idx, res):
    global max_result, min_result

    # 기저사례
    if idx == N :
        max_result = max(max_result, res)
        min_result = min(min_result, res)
        return 
    

    ret = 0
    for i in range(4):

        if op[i] > 0: # 해당 연산자가 있다면
            op[i] -= 1 # 이거 원복도 해야

            if i == 0:
                go(idx + 1, res + nums[idx])
            elif i == 1:
                go(idx + 1, res - nums[idx])
            elif i == 2:
                go(idx + 1, res * nums[idx])
            elif i == 3:
                if res < 0:
                    go(idx + 1, -(abs(res) // nums[idx]))
                else:
                    go(idx + 1, res // nums[idx])

            op[i] += 1 # 연산자 복구(백트래킹)

    return ret
    


go(1, nums[0])

print(max_result)
print(min_result)

