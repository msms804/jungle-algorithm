# 골드바흐의 추측
# 에라토스테네스 체 (이부분은 다시 해봐야할듯)
# 이중for문은 시간초과 떠서 투포인터로 해야

# 7184ms
T = int(input())

import math

for i in range(T):
    # 1. 에라토스테네스의 체로 거른다
    N = int(input())
    arr = [True for i in range(N + 1)] # 처음엔 모든 수가 소수인것으로 초기화(True)
    arr[0] = False

    for i in range(2, int(math.sqrt(N)) + 1):
        if arr[i]:  # 소수라면
            for j in range(i * i, N + 1, i):  # 배수 제거 최적화
                arr[j] = False

    prime_nums = []

    # 2. 에라토스테네스로 배열 만들기
    for i in range(2, N + 1):
        if arr[i] :
            prime_nums.append(i)
    
    # 3. 골드바흐 파티션 구하기 -> 이중for문은 시간초과(시간복잡도가 O(N^2))
    # for i in range(len(prime_nums)):
    #     for j in range(i, len(prime_nums)):
    #         if(prime_nums[i] + prime_nums[j] == N):
    #             n1 = prime_nums[i]
    #             n2 = prime_nums[j]
    
    # 3 - 1. 투포인터 (시간복잡도 O(N))
    l, r = 0, len(prime_nums) - 1
    ret1, ret2 = 0, 0

    while(l <= r):
        if(prime_nums[l] + prime_nums[r] == N):
            ret1 = prime_nums[l]
            ret2 = prime_nums[r]
            l += 1
            r -= 1
        elif prime_nums[l] + prime_nums[r] < N:
            l += 1
        else:
            r -= 1
            
    # 4. 출력
    print(ret1, ret2)            
